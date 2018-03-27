from rest_framework import serializers
from medias.models import Media
from accounts.models import Account

class MediaSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Media
		fields = ('url', 'pk', 'uuid', 'user', 'media', 
			'title', 'description')

