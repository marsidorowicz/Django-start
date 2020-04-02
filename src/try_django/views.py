from django.http import HttpResponse
from django.shortcuts import render



def home_page(request):
	titleIndex = "Wynajem i zarządzanie apartamentami w Polsce"
	# django_rendered_doc = "<H1>{{title}}</H1>".format(title=titleIndex)
	return render(request, "index.html", {"tittle": titleIndex})

def about_page(request):
	return render(request, "about.html", {"tittle": "O nas"})

def contact_page(request):
	return render(request, "index.html", {"tittle": "Kontakt"})