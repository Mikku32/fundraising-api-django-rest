from rest_framework import serializers

from api.models import  User, Donation, Project


class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = User
        fields = '__all__'






class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class ProjectGetSerializer(ProjectSerializer):
    user = UserSerializer()        
   







class DonationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Donation
        fields = '__all__'
class DonationGetSerializer(DonationSerializer):
    user = UserSerializer()
    project = ProjectSerializer()


