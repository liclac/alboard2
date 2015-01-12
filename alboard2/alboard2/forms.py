from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

class ProfileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']
	
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-sm-2'
		self.helper.field_class = 'col-sm-10'
		self.helper.layout = Layout(
			'username', 'first_name', 'last_name',
			FormActions(
				Submit('submit', _(u"Save"))
			)
		)
