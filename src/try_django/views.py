from django.http import HttpResponse
from django.shortcuts import render



def home_page(request):
	return render(request, "index.html")

def about_page(request):
	return HttpResponse("<h1>Wynajem i zarządzanie apartamentami\O nas\</h1>")

def contact_page(request):
	return HttpResponse("<h1>Wynajem i zarządzanie apartamentami\Kontakt</h1>")