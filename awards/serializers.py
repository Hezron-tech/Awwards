from rest_framework import serializers
from .models import Profile,Project,Moringa
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
    
# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False, read_only=True)
#     class Meta:
#         model = Profile
#         fields = ['id','user', 'profile_pic', 'bio', 'contact']

class ProjectSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Moringa
        fields = ['id','title', 'url','description']