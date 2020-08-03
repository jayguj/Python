from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import request
from .models import UserDetails,Requests,User_Responses
from.serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
import random
# Create your views here.
@csrf_exempt
def login(request):  #authentication

    if request.method == 'GET':
        udetails = UserDetails.objects.all()
        serializer = UserSerializers(udetails, many=True)
        # print(request.GET.get('email'))
        print(serializer['first_name'])
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(type(data))
        print(data['email'])

        lt=[]
        uemail=list(UserDetails.objects.values('email'))
        upassword=list(UserDetails.objects.values('password'))

        for d in uemail:
            for v in d.values():
                lt.append(v)
        print(lt)

        for k in range(len(lt)):
            if data['email'] == lt[k]:
                print("Hello")
                p=UserDetails.objects.filter(email=data['email'])
                print(p)
                serializer = UserSerializers(p, many=True)
                return JsonResponse(serializer.data, safe=False)
        return HttpResponse("Please Register!!!")


@csrf_exempt
def message(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        print(data['user_id'])
        print(data['user_message'])
        user_id=data['user_id']
        user_message=data['user_message']
        try:
            a=Requests(user_id=UserDetails.objects.get(user_id=user_id),user_message=user_message)
            a.save()
            va=[]
            options=list(User_Responses.objects.filter(message=user_message).values('opt1','opt2','opt3','opt4'))
            for d in options:
                for v in d.values():
                    va.append(v)
            result_response=random.choice(va)
            return JsonResponse({'res':result_response,
            'user_id':data['user_id']})
        except UserDetails.DoesNotExist:
            return HttpResponse("User doesn't exist")

# @csrf_exempt
# def uResponse(request):
#     if request.method == "GET":
#         k=[]
#         va=[]
#         # data=list(User_Responses.objects.values('message'))
#         options=list(User_Responses.objects.filter(message='Hi').values('opt1','opt2','opt3','opt4'))
#         # rdict={}
#         # ''
#         # for d in data:
#         #     for v in d.values():
#         #         k.append(v)
#         # print(k)
#         #
#         for d in options:
#             for v in d.values():
#                 va.append(v)
#         print(va)
#         result_response=random.choice(va)
#
#
#
#
#         # print(type(data))
#         # print(data)
#         # print(options)
#
#     return HttpResponse("Hello!!!")
