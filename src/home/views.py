from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse(f"Bienvenue {request.user.email}")
    #return render(request, "home/home.html")