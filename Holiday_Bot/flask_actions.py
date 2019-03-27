from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests
import json
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from datetime import datetime
from flask import Flask, render_template
#Init app
app=Flask(__name__)


#basedir=os.path.abspath(os.path.dirname(__file__))

#Database
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/Holidays'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#Init db
db=SQLAlchemy(app)
#Init marshmallow
ma=Marshmallow(app)

# @app.route('/')
# def home():
#     return render_template('index.html')

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
		fields=['holiday_date','event']

holidaysSchema=HolidaySchema(many=True)

class ActionHoliday(Action):
	def name(self):
		return 'action_holiday'
	def run(self, dispatcher, tracker, domain):
		day = tracker.get_slot('day')
		k=u"weekend"
		if (day =="weekdays") | (day == "weekday"):
			queryset=Holiday.query.filter(Holiday.holiday_date>=datetime.now(),Holiday.is_Weekday=='True').with_entities(Holiday.holiday_date,Holiday.event).order_by(Holiday.holiday_date).limit(5) #for number of holidays given by user
			result=holidaysSchema.dump(queryset)
			print(type(result))
			print(result)
			#response=json.dumps(result.data[0]) #only for one holiday
			response=json.dumps(result.data)
			print(type(response))
			dispatcher.utter_message(response)


		elif (day == "weekends") | (day == "weekend"):
			queryset=Holiday.query.filter(Holiday.is_Weekday=='False' , Holiday.holiday_date>=datetime.utcnow()).with_entities(Holiday.holiday_date,Holiday.event).order_by(Holiday.holiday_date).limit(5) #for number of holidays given by user
			print(datetime.now())
			result=holidaysSchema.dump(queryset)
			print(type(result))
			print(result)
			#response=json.dumps(result.data[0]) #only for one holiday
			response=json.dumps(result.data)
			print(type(response))
			dispatcher.utter_message(response)

		return [SlotSet("day",day)]

#Run server
if __name__=="__main__":
    app.run(debug=True)
