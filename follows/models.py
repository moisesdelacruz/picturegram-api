from django.db import models
from accounts.models import Account
# Create your models here.

class Follow(models.Model):

	user_follower = models.ForeignKey(Account, verbose_name='Usuario Seguidor',
						on_delete=models.CASCADE, related_name="%(class)suser_follower")
	user_followed = models.ForeignKey(Account, verbose_name='Usuario Seguido', 
						on_delete=models.CASCADE, related_name="%(class)suser_followed")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {}'.format(self.user_follower, self.user_followed)