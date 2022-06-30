from django.shortcuts import render, get_object_or_404
from actualites.models import Actualite

def actualites(request):

	# requetes
	actualites = Actualite.objects.all().order_by('-date')

	template = 'actualites/actualites.html'
	context = {
		'actualites' : actualites,

		'title_page' : 'Actualités',
	}

	return render(request, template, context)


def detail(request, id):

	# requetes
	actualite = get_object_or_404(Actualite, pk=id)

	template = 'actualites/detail.html'
	context = {
		'actualite' : actualite,

		'title_page' : 'Detail',
	}

	return render(request, template, context)
