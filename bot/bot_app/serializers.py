from rest_framework import serializers
from .models import UserDetails

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        #fields=('firstname' , 'lastname')
        fields='__all__'
