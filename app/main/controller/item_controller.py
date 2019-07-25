from flask import request, g 
from flask_restplus import Resource
from flask_restplus.marshalling import marshal

from ..util.dto import ItemCreateDto, ItemDto, ItemDetailDto, ItemUpdateDto
from ..service import item_service
from ..util.decorator import Authenticate

api = ItemDto.api
item = ItemDto.item
item_create = ItemCreateDto.item
item_detail = ItemDetailDto.item
item_update = ItemUpdateDto.item


parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('/')
@api.response(404, 'no items found')
class ItemList(Resource):

    @api.doc('List of items')
    @Authenticate
    def get(self):
        items = item_service.get_all_items()
        if len(items) == 0:
            return {'status' : 'no items found'}, 404
        return marshal(items, item)
    
    @api.response(201, 'Item Created')
    @api.doc('create new item')
    @api.expect(item_create, validate=True)
    @Authenticate
    @api.expect(parser)
    def post(self):
        data = request.json
        data['owner_id'] = g.user['owner_id']
        return item_service.create_item(data)

@api.route('/<item_id>')
@api.param('item_id', 'items unique id')
@api.response(404, 'item not found')
@api.response(401, 'owner_id mismatch')
class Item(Resource):

    @api.doc('get item by ID')
    @api.marshal_with(item_detail)
    @Authenticate
    def get(self, item_id):
        data = request.json
        return item_service.get_item_by_id(item_id)
    
    @api.doc('update item by id')
    @api.expect(item_update, validate=True)
    @api.marshal_with(item_update)
    @Authenticate
    def put(self, item_id):
        data = request.json
        owner_id = g.user.get('owner_id')
        item = item_service.get_item_by_id(item_id)
        print(item)
        if not item:
            api.abort(404)
        if owner_id != item.owner_id:
            api.abort(401)
        return item_service.update_item(item_id, data)
    
    @api.doc('delete item by id')
    @Authenticate
    def delete(self, item_id):
        if g.user.get('owner_id') != item_service.get_item_by_id(item_id).owner_id:
            api.abort(401)
        
        return item_service.delete_item(item_id)
       
    