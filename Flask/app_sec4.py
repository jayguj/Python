from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from itemsec5 import Item,ItemList
from user import UserRegister
app = Flask(__name__)
app.secret_key='jay'
api=Api(app)
jwt=JWT(app, authenticate,identity)   #JWT creates an endpoint called /auth

# items=[]
# class Item(Resource):
#     parser=reqparse.RequestParser()
#     parser.add_argument('price',
#     type=float,
#     required=True,
#     help='This field cannot be left blank')
#     # @app.route('/student/<string:name>')
#     @jwt_required()
#     def get(self,name):
#         # for item in items:
#         #     if item['name']==name:
#         #         return item
#         item=next(filter(lambda x:x['name']==name,items),None)
#         return {'item':item}, 200 if item else 404
#
#     def post(self,name):
#         if next(filter(lambda x:x['name']==name,items),None) is not None:
#             return {'message':"An item with '{}' already exists".format(name)},400
#         # data=request.get_json()
#         data=Item.parser.parse_args()
#         item={'name':name,'price':data['price']}
#         items.append(item)
#         print(items)
#         return item,201
#
#     def delete(self,name):
#         global items
#         items=list(filter(lambda x:x['name'] !=name,items))
#         return {'message':'item deleted'}
#         # parser=reqparse.RequestParser()
#         # parser.add_argument('price',
#         # type=float,
#         # required=True,
#         # help='This field cannot be left blank')
#     def put(self,name):
#         # data=request.get_json()
#         data=Item.parser.parse_args()
#         item=next(filter(lambda x:x['name']==name,items),None)
#         if item is None:
#             item={'name':name,'price':data['price']}
#             items.append(item)
#         else:
#             item.update(data)
#         return item
#
#
#
# class ItemList(Resource):
#     def get(self):
#         return {'Items':items}
api.add_resource(Item,'/item/<string:name>')  #http://localhost:5000/student/Jay
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

app.run(port=5000)
