from django.db import models
from ckeditor.fields import RichTextField

class Actualite(models.Model):
	image = models.FileField(upload_to='images-actualites/')
	titre = models.CharField(max_length=100)
	description = RichTextField()
	newsLetter = models.BooleanField(default=False)

	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Actualité : {self.titre}"
