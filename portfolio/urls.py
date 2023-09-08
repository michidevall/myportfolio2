from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'education',views.EducationViewSet)
router.register(r'work',views.WorkViewSet)
router.register(r'portfolio',views.PortfolioViewSet)
urlpatterns = [
    path('', include(router.urls)),
]