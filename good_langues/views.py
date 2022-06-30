from django.shortcuts import render, redirect
from django.contrib import messages
from good_langues.models import CoachGoodLangue, Session, Preinscription
from good_langues.forms import PreinscriptionForm

def about_good_lagues(request):
	# requetes
	equipe_good_langues = CoachGoodLangue.objects.all()
	
	# variable pour les components
	titre_equipe = 'Nos coachs'
	description_equipe = "Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate."

	template = 'good_langues/about_good_lagues.html'
	context = {
		'equipe' : equipe_good_langues,
		
		'titre_equipe' : titre_equipe,
		'description_equipe' : description_equipe,

		'title_page' : 'Good Langues',
	}

	return render(request, template, context)

def preinscription_good_langue(request):
	
	# requetes
	session = Session.objects.all().last()

	if session == None:
		return redirect('about-good-lagues')

	if request.method == 'POST':
		
		anglais = request.POST.get('anglais')
		chinois = request.POST.get('chinois')
		espagnol = request.POST.get('espagnol')
		italien = request.POST.get('italien')

		form = PreinscriptionForm(request.POST)

		if form.is_valid():
			
			langues = ""

			if anglais:
				langues +=  f"{anglais} "
			if chinois:
				langues +=  f"{chinois} "
			if espagnol:
				langues +=  f"{espagnol} "
			if italien:
				langues +=  f"{italien} "
			
			form.instance.session_id = session.id
			form.instance.langues = langues

			if len(langues) > 0:
				form.save()
				messages.success(request, f"Préinscription réussie ! Nous vous contacterons dès que possible pour vous inscrire à la session de {session.libelle}")
				return redirect('preinscription-good-langues')
			else:
				messages.error(request, f"Oupss... Veuillez choisir au moin une langue.")
				return redirect('preinscription-good-langues')
		else:
			messages.error(request, f"Oupss... Veuillez remplir tous les champs.")
			return redirect('preinscription-good-langues')

	template = 'good_langues/preinscription.html'
	context = {
		'session' : session.libelle,

		'title_page' : 'Preinscription',
	}

	return render(request, template, context)