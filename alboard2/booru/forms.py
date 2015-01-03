from django.utils.translation import ugettext as _
from django import forms
from .models import *

class PoolForm(forms.ModelForm):
	class Meta:
		model = Pool
		fields = ['name', 'start_date', 'end_date']
		widgets = {
			'name': forms.TextInput(attrs={'autofocus': 'autofocus'}),
			'start_date': forms.DateInput(attrs={'placeholder': _("YYYY-MM-DD")}),
			'end_date': forms.DateInput(attrs={'placeholder': _("YYYY-MM-DD")}),
		}
