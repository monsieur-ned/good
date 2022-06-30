from django.db import models

class EquipeGood(models.Model):
	profil = models.FileField(upload_to = 'profil-good/')
	nom = models.CharField("Nom complet : ", max_length=100)
	fonction = models.CharField(max_length=50)

	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.fonction} - {self.nom}"


class NewsLetter(models.Model):
	email = models.EmailField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email