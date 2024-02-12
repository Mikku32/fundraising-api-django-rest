from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.hashers import check_password

from api.models import Donation,  Project, CustomUser
from api.serializers import DonationGetSerializer, DonationSerializer, ProjectGetSerializer, ProjectSerializer, CustomUserSerializer

# Create your views here.
# views.py


class UserRegister(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserList(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
        
       


class UserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.filter(email=email).first()

        if user is None or not check_password(password,user.password):
            return Response({'error': 'Invalid email/password combination'}, status=status.HTTP_400_BAD_REQUEST)

        # You can implement JWT token authentication here or any other authentication mechanism

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


   

    

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectGetSerializer
        else:
            return ProjectSerializer
     

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectGetSerializer
        else:
            return ProjectSerializer





class DonationList(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return DonationGetSerializer
        else:
            return DonationSerializer
        



class DonationDetail(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Donation.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return DonationGetSerializer
        else:
            return DonationSerializer


