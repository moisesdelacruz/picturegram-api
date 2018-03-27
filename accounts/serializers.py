from rest_framework import serializers
from accounts.models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Account
		fields = ('url', 'pk', 'username', 'uuid', 'first_name', 
			'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')