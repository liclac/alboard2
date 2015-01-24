from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import *

class ProfileView(DetailView):
	model = User
	
	def get_object(self, queryset=None):
		return self.request.user

class ProfileUpdateView(UpdateView):
	model = User
	form_class = ProfileForm
	success_url = reverse_lazy('account_profile')
	
	def get_object(self, queryset=None):
		return self.request.user

class ProfileDeleteView(DeleteView):
	model = User
	success_url = reverse_lazy('posts')
	
	def get_object(self, queryset=None):
		return self.request.user
