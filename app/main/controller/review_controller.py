from flask import request, g
from flask_restplus import Resource
from flask_restplus.marshalling import marshal

from ..util.dto import ReviewCreateDto, ReviewDto, ReviewDetailDto, ReviewUpdateDto
from ..service import review_service
from ..util.decorator import Authenticate

api = ReviewDto.api
review = ReviewDto.review
review_create = ReviewCreateDto.review
review_detail = ReviewDetailDto.review
review_update = ReviewUpdateDto.review


parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('/')
@api.response(404, 'no items found')
class ReviewList(Resource):

    @api.doc('List of Reviews')
    def get(self):
        reviews = review_service.get_all_reviews()
        if len(reviews) == 0:
            return {'status' : 'no reviews found'}, 404
        return marshal(reviews, review)
    
    @api.response(201, 'Review Created')
    @api.doc('create new review')
    @Authenticate
    @api.expect(parser)
    def post(self):
        data = request.json
        data['owner_id'] = g.user['owner_id']
        return review_service.create_review(data)

@api.route('/<review_id>')
@api.param('review_id', 'reviews unique id')
@api.response(404, 'review not found')
@api.response(401, 'ownder_id mismatch')
class Review(Resource):

    @api.doc('get review by ID')
    @api.marshal_with(review_detail)
    @Authenticate
    def get(self, review_id):
        data = request.json
        return review_service.get_review_by_id(review_id)
    
    @api.doc('update review by id')
    @api.expect(review_update, validate=True)
    @api.marshal_with(review_update)
    @Authenticate
    def put(self, review_id):
        data = request.json
        owner_id = g.user.get('owner_id')
        review = review_service.get_review_by_id(review_id)
        if not review:
            api.abort(404)
        if owner_id != review.owner_id:
            api.abort(401)
        return review_service.update_review(review_id, data)
    
    @api.doc('delete review by id')
    @Authenticate
    def delete(self, review_id):
        if g.user.get('owner_id') != review_service.get_review_by_id(review_id).owner_id:
            api.abort(401)
        
        return review_service.delete_review(review_id)