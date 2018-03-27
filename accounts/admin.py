# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group
# Register your models here.
@admin.register(Account)
class UserAdmin(UserAdmin):

	list_display = ('uuid', 'first_name', 'last_name')
	fieldsets = (
		(None, {
			'fields': ('username', 'password')}),
		(_('Personal info'), {
			'fields': ('first_name', 'last_name', 'date_of_birth')}),
		(_('Permissions'), {
			'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		(_('Important dates'), {
			'fields': ('last_login', 'date_joined')}),
		)
	add_fieldsets = (
		(None, {
		'classes': ('wide',),
		'fields': ('username', 'password1', 'password2')}),
		(_('Personal info'), {
			'fields': ('first_name', 'last_name', 'date_of_birth')}),
		(_('Permissions'), {
		'classes': ('wide',),
		'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		(_('Important dates'), {
		'classes': ('wide',),
		'fields': ('last_login', 'date_joined')}),
		)

	search_fields = ('username', 'name', 'email')
	ordering = ('pk',)
	filter_horizontal = ()

