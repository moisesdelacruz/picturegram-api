from django.shortcuts import render
from rest_framework import viewsets
from likes.models import Like
from likes.serializers import LikeSerializer
# Create your views here.

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer