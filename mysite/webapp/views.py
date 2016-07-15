from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm


def index(request):
	template_name = 'webapp/home.html'
	context = {}
	return render(request, template_name, context)
	
def projects(request):
	template_name = "webapp/projects.html"
	context = {}
	return render(request, template_name, context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		from_email = form.cleaned_data.get("from_email")
		subject = form.cleaned_data.get("subject")
		message = form.cleaned_data.get("message")
		recipient_list = [settings.EMAIL_HOST_USER]
		
		# print(from_email)
		# print(subject)  
		# print(message) 
		# print(recipient_list)
	
		send_mail(
			subject,
			message,
			from_email,
			recipient_list,
			fail_silently=False)
		

	template_name = 'webapp/contact.html'
	context = {'form': form}
	return render(request, template_name, context)
	
	