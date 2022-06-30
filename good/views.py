from django.shortcuts import render
from good.models import NewsLetter
from good.forms import NewsLetterForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def addNewsLetter(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		form_news = NewsLetterForm(request.POST)

		print(form_news.instance)
		print(NewsLetter.objects.filter(email=email).exists())

		if NewsLetter.objects.filter(email=email).exists() == False:
			
			if form_news.is_valid():
				form_news.save()
				messages.success(request, "Adresse enregistrée avec succès !")
				return HttpResponseRedirect('/')

		else:
			messages.error(request, "L'addresse email existe déjà dans la base de donnée !")
			return HttpResponseRedirect('/')
	form = NewsLetterForm()
	return HttpResponseRedirect('/')