from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Pool, Post

class PoolView(DetailView):
	model = Pool

class PostView(DetailView):
	model = Post
