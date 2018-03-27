from rest_framework import serializers
from likes.models import Like

class LikeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Like
		fields = ('url', 'pk', 'user', 'media')