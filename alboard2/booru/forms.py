from django.utils.translation import ugettext as _
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
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
	
	def __init__(self, *args, **kwargs):
		super(PoolForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-sm-2'
		self.helper.field_class = 'col-sm-10'
		self.helper.layout = Layout(
			'name', 'start_date', 'end_date',
			FormActions(
				Submit('submit', u"Save")
			)
		)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['pool', 'image', 'description', 'signature', 'tags']
	
	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-sm-2'
		self.helper.field_class = 'col-sm-10'
		self.helper.layout = Layout(
			'pool', 'image', 'description', 'signature', 'tags',
			FormActions(
				Submit('submit', u"Save")
			)
		)

class PostUpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['pool', 'description', 'tags']
	
	def __init__(self, *args, **kwargs):
		super(PostUpdateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-sm-2'
		self.helper.field_class = 'col-sm-10'
		self.helper.layout = Layout(
			'pool', 'description', 'tags',
			FormActions(
				Submit('submit', u"Save")
			)
		)
