from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import json
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)
ma = Marshmallow(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/Holidays'
db = SQLAlchemy(app)

class Holiday(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement = True)
    holiday_date=db.Column(db.DateTime,unique=True,nullable=False,default=datetime.utcnow)
    is_Weekday=db.Column(db.String)
    event = db.Column(db.String, default='Weekend')
    def __init__(self,holiday_date,is_Weekday):
        self.holiday_date=holiday_date
        self.is_Weekday=is_Weekday


class HolidaySchema(ma.Schema):
    class Meta:
        model = Holiday
        fields = ('id','holiday_date','event')

holiday_schema = HolidaySchema(many=True,strict=True)

@app.route('/get')
def get_json():
    search_str='True'
    present = datetime.now()
    print(present)
    result = Holiday.query.filter(Holiday.is_Weekday.contains(search_str))
    result1 = result.filter(Holiday.holiday_date>= present)
    print(datetime.utcnow())
    #output = holiday_schema.dump(first).data
    return (holiday_schema.jsonify(result1))

if __name__ == '__main__':
    app.run(debug=True)
