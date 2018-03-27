from django.db import models
from accounts.models import Account
from utils.storage import content_file_name
import uuid
# Create your models here.

class Media(models.Model):
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	user = models.ForeignKey(Account, verbose_name='Usuarios', on_delete=models.CASCADE)
	media = models.FileField('media', blank=False, upload_to=content_file_name)
	title = models.CharField('Titulo', blank=True, null=True, max_length=100)
	description = models.TextField('Descripcion', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.user.pk)

	def media_url(self):
		if self.media:
			return self.media.url
		else:
			return 'http://americanconstruction.net/wp-content/uploads/2015/10/upload-empty.png'