from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post

class PostAdd(CreateView):
	model = Post 
	fields = ['title', 'body']