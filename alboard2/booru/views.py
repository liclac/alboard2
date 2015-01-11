from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

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
	form_class = PoolForm
	fields = ['pool', 'description', 'tags']
	context_object_name = 'pool'

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

class PostsView(ListView):
	model = Post
	paginate_by = 30
	context_object_name = 'posts'

class PostCreateView(CreateView):
	model = Post
	form_class = PostForm
	
	def get_initial(self):
		data = {}
		
		if 'pid' in self.kwargs:
			try:
				data['pool'] = Pool.objects.get(pk=self.kwargs['pid'])
			except Pool.DoesNotExist:
				pass
		
		return data

class PostUpdateView(UpdateView):
	model = Post
	form_class = PostUpdateForm
	context_object_name = 'post'
