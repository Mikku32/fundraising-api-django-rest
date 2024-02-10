from django.shortcuts import render
from rest_framework import generics

from api.models import Donation,  Project, User
from api.serializers import DonationGetSerializer, DonationSerializer, ProjectGetSerializer, ProjectSerializer, UserSerializer

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer






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


