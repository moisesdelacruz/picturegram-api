from django.contrib import admin
from medias.models import Media
# Register your models here.

@admin.register(Media)
class MediaList(admin.ModelAdmin):
	list_display = ('user', 'title', 'media_url')

	def media_url(self, obj):
		url = obj.media_url()
		tag = '<img src="%s" width="50"/>' % url
		return tag

	media_url.allow_tags = True
	media_url.admin_order_field = 'media'
