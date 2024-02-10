from rest_framework import serializers

from api.models import  User, Donation, Project


class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Project
        fields = '__all__'

        

        

class DonationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    project = ProjectSerializer()
    class Meta:
        model = Donation
        fields = '__all__'

