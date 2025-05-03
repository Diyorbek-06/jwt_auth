from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from yaml import serialize
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.



class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({"data": user.username, 'msg': "siz royxat otdingiz"})



        # def post(self, request):
    #     serializer = RegisterSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"data": serializer.data, 'msg':"siz royxat otdingiz"})
    #     return Response({"msg":"xatolik", 'status':400})

class Test(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        return Response({'msg':"nimadir"})


