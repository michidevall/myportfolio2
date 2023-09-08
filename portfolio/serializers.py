from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from .models import Education, Work, Portfolio


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        
class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
        
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'