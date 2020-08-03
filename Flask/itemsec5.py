from flask_restful import Resource,reqparse
import sqlite3
from flask_jwt import jwt_required
class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help='This field cannot be left blank')
    # @app.route('/student/<string:name>')
    @jwt_required()
    def get(self,name):
        # for item in items:
        #     if item['name']==name:
        #         return item
        # item=next(filter(lambda x:x['name']==name,items),None)
        # return {'item':item}, 200 if item else 404
        connection=sqlite3.connect('sec5data.db')
        cursor=connection.cursor()
        query="SELECT * FROM items WHERE name=?"
        cursor.execute(query,(name,))
        row=cursor.fetchone()
        connection.close()
        if row:
            return{'item':{'name':row[0],'price':row[1]}}
        return {'message':"Item not found"},404

    def post(self,name):
        if next(filter(lambda x:x['name']==name,items),None) is not None:
            return {'message':"An item with '{}' already exists".format(name)},400
        # data=request.get_json()
        data=Item.parser.parse_args()
        item={'name':name,'price':data['price']}
        items.append(item)
        print(items)
        return item,201

    def delete(self,name):
        global items
        items=list(filter(lambda x:x['name'] !=name,items))
        return {'message':'item deleted'}
        # parser=reqparse.RequestParser()
        # parser.add_argument('price',
        # type=float,
        # required=True,
        # help='This field cannot be left blank')
    def put(self,name):
        # data=request.get_json()
        data=Item.parser.parse_args()
        item=next(filter(lambda x:x['name']==name,items),None)
        if item is None:
            item={'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'Items':items}
