from app.main.model.user import User
from ..service.blacklist_service import save_token
from .. import db


class Auth:

    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200

            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match'
                }
                return response_object, 401
        
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            resp = User.decode_auth_token(data)
            if not isinstance(resp, str):
                #mark the token as blacklisted
                return save_token(token=data)
            else:
                response_object = {
                    'status' : 'fail',
                    'message' : resp
                }
                return response_object, 401
        else:
            response_object = {
                'status' : 'fail',
                'message' : 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        #get the auth token
        #stored in headers, key or 'Authorization'
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token'
            }
            return response_object, 401
    
    
    # @staticmethod
    # def delete_user(data, auth_token):
    #     if auth_token:
    #         resp = User.decode_auth_token(auth_token)
    #         try:
    #             user = User.query.filter_by(email=data.get('email')).first()
    #             if user and user.check_password(data.get('password')):
    #                 db.session.delete(user)
    #                 db.session.commit()
    #                 response_object = {
    #                     'status': 'success',
    #                     'message': 'Successfully deleted'
    #                 }
    #                 return response_object, 200
    #         except Exception as e:
    #             response_object = {
    #                 'status': 'fail',
    #                 'message': e
    #             }
    #             return response_object, 401
    #     else:
    #         response_object = {
    #             'status': 'fail',
    #             'message': 'Provide an auth token'
    #         }
    #         return response_object, 401
