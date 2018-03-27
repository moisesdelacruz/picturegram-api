from django.shortcuts import render
from rest_framework import viewsets
from medias.models import Media
from medias.serializers import MediaSerializer
# Create your views here.

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer