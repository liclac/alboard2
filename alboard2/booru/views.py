from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pool, Post
from .forms import PoolForm

class PoolView(DetailView):
	model = Pool
	context_object_name = 'pool'
	
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['active_year'] = self.object.start_date.year
		
		return context

class PoolCreateView(CreateView):
	model = Pool
	form_class = PoolForm

class PoolUpdateView(UpdateView):
	model = Pool
	fields = ['name', 'start_date', 'end_date']

class PostView(DetailView):
	model = Post
	context_object_name = 'post'
	
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['pool'] = self.object.pool
		context['active_year'] = self.object.pool.start_date.year
		context['prev_post'] = Post.objects.filter(pool=self.object.pool).filter(created_at__lt=self.object.created_at).order_by('-created_at').first()
		context['next_post'] = Post.objects.filter(pool=self.object.pool).filter(created_at__gt=self.object.created_at).order_by('created_at').first()
		
		return context
