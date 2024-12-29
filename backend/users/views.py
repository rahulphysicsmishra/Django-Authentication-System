from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    query_set = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    