from rest_framework import serializers

from api.models import  CustomUser, Donation, Project


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        return user




class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class ProjectGetSerializer(ProjectSerializer):
    user = CustomUserSerializer()        
   







class DonationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Donation
        fields = '__all__'
class DonationGetSerializer(DonationSerializer):
    user = CustomUserSerializer()
    project = ProjectSerializer()


