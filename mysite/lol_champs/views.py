from django.shortcuts import render
from .scraper import get_lol_champs

def index(request):
	lol_champs = get_lol_champs()
	template_name = 'lol_champs/index.html'
	context = { 
		'roster': lol_champs[0],
		'rotation': lol_champs[1]
	}
	return render(request, template_name, context)