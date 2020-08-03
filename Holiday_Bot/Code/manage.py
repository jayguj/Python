from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/Holidays'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    holiday_date=db.Column(db.DateTime,unique=True,nullable=False,default=datetime.utcnow)
    is_Weekday=db.Column(db.String)
    event = db.Column(db.String)

if __name__ == '__main__':
    manager.run()
