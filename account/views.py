from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from yaml import serialize
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
import datetime

# Create your views here.



class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({"data": user.username, 'msg': "siz ro'yxat o'tdingiz"})



    #     def post(self, request):
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


class LoginView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        else:
            ip = request.META.get('REMOTE_ADDR')
            with open("failed_logins.txt", "a") as f:
                f.write(f"[{datetime.datetime.now()}]  Failed login: username='{username}', IP='{ip}'\n")

            return Response({
                'error': "Login yoki parol noto‘g‘ri"
            }, status=401)


class Logout(APIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication,]
    def post(self, request):
        data = request.data
        refresh = RefreshToken(data['refresh'])
        refresh.blacklist()
        return Response({
            'msg':'Tizimdan chiqdingiz'
        })


