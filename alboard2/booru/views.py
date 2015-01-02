from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Pool, Post

class PoolView(DetailView):
	model = Pool
	
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['active_year'] = context['object'].start_date.year
		return context

class PostView(DetailView):
	model = Post
	
	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['active_year'] = context['object'].pool.start_date.year
		return context
