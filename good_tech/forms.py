from django.forms import ModelForm
from good_tech.models import Preinscription

class PreinscriptionForm(ModelForm):
	class Meta:
		model = Preinscription
		fields = [
			'nom',
			'prenom',
			'genre',
			'telephone',
		]