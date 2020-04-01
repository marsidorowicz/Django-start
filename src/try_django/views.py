from django.http import HttpResponse


def home_page(request):
	return HttpResponse("<h1>Wynajem i zarządzanie apartamentami</h1>")