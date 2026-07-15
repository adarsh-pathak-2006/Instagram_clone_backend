from django.shortcuts import render, get_object_or_404
from auth.serializers import ProfileSerializer, UserSerializer, RegisterSerializer
from auth.models import Profile
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView


class RegisterAPI(APIView):
    def post(self, request):
        serial=RegisterSerializer(data=request.data)
        if serial.is_valid:
            f_name=serial.validated_data['first_name']
            l_name=serial.validated_data['last_name']
            username=serial.validated_data['username']
            email=serial.validated_data['email']
            password=serial.validated_data['password']

            if User.objects.filter(username=username).exists():
                return Response({ 'message':'User already exists' })
            else:
                user_data=User.objects.create_user(first_name=f_name, last_name=l_name, username=username, email=email, password=password)
                Profile.objects.create(user=user_data, name=f_name+" "+l_name)
                return Response({ 'message':'registration successfull' })
        else:
            return Response({ 'invalid':'invalid inputs' })
        
class ProfileAPI(RetrieveUpdateAPIView):
    serializer_class=ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)