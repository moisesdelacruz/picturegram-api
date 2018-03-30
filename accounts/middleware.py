# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import login as login_user
from rest_framework.authtoken.models import Token


class LoginUserByToken(MiddlewareMixin):
    """
    This middleware logged user by token.
    """
    def process_request(self, request):
        if not request.user.is_authenticated:
            token = request.GET.get('token_id', None)
            if token:
                try:
                    token = Token.objects.get(key=token)
                    user = token.user
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    login_user(request, user)
                except Token.DoesNotExist:
                    pass


class DisableCSRF(MiddlewareMixin):
    """
    This middleware disabled globally CSRF feature.
    """
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
