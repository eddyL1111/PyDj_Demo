from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect 
from django.views.generic import View
from .forms import UserForm, LoginForm

def index(request):
	if request.user.username is None:
		username = request.user.username 
	else:
		username = 'test'
			
	template_name = 'authentication/index.html'
	context = {'username': username}
	return render(request, template_name, context)

def LogoutView(request):
	logout(request)
	return redirect('../login')
	
class LoginForm(View):
	loginForm_class = LoginForm
	
	def get(self, request):
		form = self.loginForm_class(None)
		template_name = 'authentication/login.html'
		context = {'form': form}
		return render(request, template_name, context)
		
	def post(self, request):
		form = self.loginForm_class(request.POST)
		
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			
			if user is not None and user.is_active:
				login(request, user)
				return redirect('/projects/auth/')

		return redirect('/') # error page
		
class SignupForm(View):
	signupForm_class = UserForm
	
	def get(self, request):
		form = self.signupForm_class(None)
		template_name = 'authentication/signup.html'
		context = {'form': form}
		return render(request, template_name, context)
	
	def post(self, request):
		form = self.signupForm_class(request.POST)
		
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
	
		return redirect('/projects/auth/login')
	
	
	
	
	
	
class UserFormView(View):
	signupForm_class = UserForm 
	loginForm_class = LoginForm
	template_name = 'authentication/index.html' 
	
	def get(self, request):
		signup_form = self.signupForm_class(None)
		login_form = self.loginForm_class(None)
		
		if request.user.username is not None:
			username = request.user.username 
		else:
			username = 'test'
		
		context = {
			'signup_form': signup_form,
			'login_form': login_form,
			'username':  username
		}
		return render(request, self.template_name, context)
		
	def post(self, request):
		signup_form = self.signupForm_class(request.POST) 
		login_form = self.loginForm_class(request.POST)
	
		if signup_form.is_valid():
			user = signup_form.save(commit=False) 
			
			username = signup_form.cleaned_data['username']
			password = signup_form.cleaned_data['password']
			user.set_password(password)
			user.save()
			
			user = authenticate(username=username, password=password)
			
			if user is not None and user.is_active:
				login(request, user)
		"""	
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			
			if user is not None:
				if user.is_active:
					login(request, user)
					logged_username = username
		"""	
		return redirect('/')