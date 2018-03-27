from django.contrib import admin
from follows.models import Follow
# Register your models here.

@admin.register(Follow)
class FollowList(admin.ModelAdmin):
	list_display = ('user_follower', 'user_followed')
