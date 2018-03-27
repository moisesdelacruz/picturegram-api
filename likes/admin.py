from django.contrib import admin
from likes.models import Like
# Register your models here.

@admin.register(Like)
class LikeList(admin.ModelAdmin):
	list_display = ('user', 'media', 'created_at')
