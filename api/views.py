from django.shortcuts import render
from rest_framework import generics

from api.models import Donation, DonationHistory, Project, User
from api.serializers import DonationHistorySerializer, DonationSerializer, ProjectSerializer, UserSerializer

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer  

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class DonationList(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class DonationDetail(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


