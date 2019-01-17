from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    #pythonn
	#python 2
#
class Requests(models.Model):
    user_id=models.ForeignKey(UserDetails,on_delete=False)
    user_message=models.CharField(max_length=500)

class User_Responses(models.Model):
    message=models.CharField(max_length=500)
    opt1=models.CharField(max_length=200)
    opt2=models.CharField(max_length=200)
    opt3=models.CharField(max_length=200)
    opt4=models.CharField(max_length=200)
