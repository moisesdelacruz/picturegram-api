from django.db import models
from accounts.models import Account
from medias.models import Media
# Create your models here.

class Like(models.Model):
	user = models.ForeignKey(Account, verbose_name='Usuario', on_delete=models.CASCADE)
	media = models.ForeignKey(Media, verbose_name='Media', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {}'.format(self.user, self.media)	    