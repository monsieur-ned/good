from django.forms import ModelForm
from good_langues.models import Preinscription

class PreinscriptionForm(ModelForm):
	class Meta:
		model = Preinscription
		fields = [
			'nom',
			'prenom',
			'genre',
			'telephone',
		]