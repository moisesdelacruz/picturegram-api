from django.db import models
from accounts.models import Account
import uuid
# Create your models here.

class Media(models.Model):
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	user = models.ForeignKey(Account, verbose_name='Usuarios', on_delete=models.CASCADE)
	media = models.URLField('media', max_length=500, blank=False)
	title = models.CharField('Titulo', blank=True, null=True, max_length=100)
	description = models.TextField('Descripcion', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.user.pk)
