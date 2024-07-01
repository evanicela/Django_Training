from django.shortcuts import render
from .models import Service


# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def service_list(request):
    all_services = Service.objects.all()
    context = {"all_services": all_services}
    return render(request, 'service.html', context)
