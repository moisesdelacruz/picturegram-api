from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers import AccountSerializer
from accounts.models import Account
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer