from django.shortcuts import render, redirect
from django.contrib import messages
from good_tech.models import CoachGoodTech, Session, Preinscription
from good_tech.forms import PreinscriptionForm

def about_good_tech(request):
	# requetes
	equipe_good_tech = CoachGoodTech.objects.all()
	
	# variable pour les components
	titre_equipe = 'Nos coachs'
	description_equipe = "Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate."

	template = 'good_tech/about_good_tech.html'
	context = {
		'equipe' : equipe_good_tech,
		
		'titre_equipe' : titre_equipe,
		'description_equipe' : description_equipe,

		'title_page' : 'Good Tech',
	}

	return render(request, template, context)

def preinscription_good_tech(request):
	
	# requetes
	session = Session.objects.all().last()

	if session == None:
		return redirect('about-good-tech')

	if request.method == 'POST':
		
		web = request.POST.get('web')
		mobile = request.POST.get('mobile')
		infographie = request.POST.get('infographie')
		video = request.POST.get('video')
		bureautique = request.POST.get('bureautique')

		form = PreinscriptionForm(request.POST)

		if form.is_valid():
			
			modules = ""

			if web:
				modules +=  f"Dev. {web} "
			if mobile:
				modules +=  f"Dev. {mobile} "
			if infographie:
				modules +=  f"{infographie} "
			if video:
				modules +=  f"Montage {video} "
			if bureautique:
				modules +=  f"{bureautique} "
			
			form.instance.session_id = session.id
			form.instance.modules = modules

			if len(modules) > 0:
				form.save()
				messages.success(request, f"Préinscription réussie ! Nous vous contacterons dès que possible pour vous inscrire à la session de {session.libelle}")
				return redirect('preinscription-good-tech')
			else:
				messages.error(request, f"Oupss... Veuillez choisir au moin un module.")
				return redirect('preinscription-good-tech')
		else:
			messages.error(request, f"Oupss... Veuillez remplir tous les champs.")
			return redirect('preinscription-good-tech')

	template = 'good_tech/preinscription.html'
	context = {
		'session' : session.libelle,

		'title_page' : 'Preinscription',
	}

	return render(request, template, context)