from django.utils.safestring import mark_safe
from django.contrib import admin
from medias.models import Media
# Register your models here.

@admin.register(Media)
class MediaList(admin.ModelAdmin):
	list_display = ('user', 'title', 'image')

	def image(self, obj):
	    return mark_safe('<image src="%s" width=50 />' % obj.media)
