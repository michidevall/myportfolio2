from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, EducationSerializer, WorkSerializer, PortfolioSerializer
from .models import Education, Work, Portfolio

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class WorkViewSet(viewsets.ModelViewSet):  
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]