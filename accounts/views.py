from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_user
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from accounts.serializers import AccountSerializer
from accounts.models import Account as User
import json
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer


@csrf_exempt
@require_POST
def login(request):
    """View login"""
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        new_user = User.objects.create_user(username,
                                            password,
                                            email=None)
        # Token for Authentcation with DRF
        token, created = Token.objects.get_or_create(user=new_user)
        user = authenticate(username=username, password=password)
        login_user(request, user)
        data = {'id': new_user.id,
                'token_id': token.pk,
                'username': new_user.username,
                'was_created': True}
        return HttpResponse(json.dumps(data))

    user = authenticate(username=username, password=password)
    if not user:
        data = {'error': 'Incorrect data'}
        response = HttpResponse(json.dumps(data))
        response.status_code = 400
        return response

    login_user(request, user)
    user = User.objects.get(username=username)

    # Token for Authentcation with DRF
    token, created = Token.objects.get_or_create(user=user)

    data = {'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'token_id': token.pk,
            'was_created': False}

    return HttpResponse(json.dumps(data))
