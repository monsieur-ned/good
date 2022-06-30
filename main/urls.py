from django.contrib import admin
from django.urls import path, re_path

from django.conf.urls.static import*
from django.conf import settings

from . views import home, about
from good.views import addNewsLetter
from actualites.views import actualites, detail
from good_langues.views import about_good_lagues, preinscription_good_langue
from good_tech.views import about_good_tech, preinscription_good_tech

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', home, name='home'),
    path('a-propos', about, name='about'),
    path('newsletter', addNewsLetter, name='addNewsLetter'),
    # re_path('.*', home)
]

# Actualites urls
urlpatterns += [
    path('actualites/', actualites, name='actualites'),
    path('actualites/<int:id>', detail, name='actualite-detail'),
]

# good langues urls
urlpatterns += [
    path('good-langues/', about_good_lagues, name='about-good-lagues'),
    path('good-langues/preinscription', preinscription_good_langue, name='preinscription-good-langues'),
]

# good tech urls
urlpatterns += [
    path('good-tech/', about_good_tech, name='about-good-tech'),
    path('good-tech/preinscription', preinscription_good_tech, name='preinscription-good-tech'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)