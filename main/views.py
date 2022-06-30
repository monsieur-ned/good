from django.shortcuts import render
from actualites.models import Actualite
from good.models import EquipeGood

def home(request):

	# requetes
	actualites = Actualite.objects.all().order_by('-date')[:4]
	actualites_count = Actualite.objects.all().count()


	template = 'index.html'
	context = {
		'actualites' : actualites,
		'actualites_count' : actualites_count,

		'title_page' : 'Accueil',

	}


	return render(request, template, context)

def about(request):

	# requetes
	equipe_good = EquipeGood.objects.all()
	
	# variable pour les components
	titre_equipe = 'Notre équipe'
	description_equipe = "Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate."

	template = 'about.html'
	context = {
		'equipe' : equipe_good,
		
		'titre_equipe' : titre_equipe,
		'description_equipe' : description_equipe,

		'title_page' : 'A Propos',
	}

	return render(request, template, context)