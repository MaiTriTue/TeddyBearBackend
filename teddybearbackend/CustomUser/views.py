import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import requests
from rest_framework import viewsets, status, permissions, generics
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from requests.exceptions import HTTPError
# from bs4 import BeautifulSoup


from .models import *
from .serializers import *
from .models import *
from django.conf import settings

# dang ky - dang nhap


class UserViewSet(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser, ]

    @action(methods=['get'], detail=False, url_path='current_user')
    def current_user(self, request):
        return Response(self.serializer_class(request.user).data)

    def get_permissions(self):
        if self.action == 'current_user':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# class RegistrationAPI(generics.GenericAPIView):
#     serializer_class = CreateUserSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             # "token": AuthToken.objects.create(user)
#         })


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser, MultiPartParser, ]

    def create(self, request):
        client_app = settings.OAUTH2_INFO
        username = request.data.get('username')
        password = request.data.get('password')
        url = 'http://' + request.get_host() + '/o/token/'
        data_dict = {
            'grant_type': 'password',
            'username': username,
            'password': password,
            'client_id': client_app['client_id'],
            'client_secret': client_app['client_secret'],
        }

        aa = requests.post(url, data=data_dict)
        data = json.loads(aa.text)
        token = data.get('access_token', '')

        if token:
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

# class Login(APIView):
#     permission_classes = [permissions.AllowAny]
#     def post(self, request, id):
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#
#             return Response(data={
#                 'username': username,
#                 'password': password
#             }, status=status.HTTP_200_OK)


# login chua xong
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         print(username)
#         print(password)
        # url = 'http://' + request.get_host() + '/o/token/'
        # data_dict = {
        #     'grant_type': 'password',
        #     'username': username,
        #     'password': password,
        #     'client_id': 'NcVlaUZ7BeFPRNBnEBcilqXNlD2McMwtiCD0MOro',
        #     'client_secret': 'DUJikxXvOuqX4n44bS2NpSvu7h9oD9QEZYMLlmRDc9mwn3z6VbJJsEOGoIF3hApT3paYujdKg5wd0Pd3Ndb6qsJWZmj34s8Hk0BILL0z4d3DNXWezZK9Wpff5aMDddh4',
        # }
        # aa = requests.post(url, data=data_dict)
        # data = json.loads(aa.text)
        # token = data.get('access_token','')
        # request.session['token'] = token
        # return  HttpResponseRedirect(reverse('index'))


# Create your views here.


# Create your views here.
