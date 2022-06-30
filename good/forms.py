from django.forms import ModelForm
from good.models import NewsLetter

class NewsLetterForm(ModelForm):
	class Meta:
		model = NewsLetter
		fields = ['email']