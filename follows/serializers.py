from rest_framework import serializers
from follows.models import Follow

class FollowSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Follow
		fields = ('url', 'pk', 'user_follower', 'user_followed')