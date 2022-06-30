from django.db import models

class CoachGoodTech(models.Model):
	profil = models.FileField(upload_to = 'profil-good/')
	nom = models.CharField("Nom complet : ", max_length=100)
	fonction = models.CharField(max_length=50)

	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.fonction} - {self.nom}"

class Session(models.Model):
	libelle = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.libelle}"

class Preinscription(models.Model):
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	genre = models.CharField(max_length=25)
	telephone = models.CharField(max_length=30)
	session = models.ForeignKey(Session, on_delete = models.CASCADE)
	modules = models.CharField(max_length=100)

	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return f"{self.nom} {self.prenom} - {self.modules}"