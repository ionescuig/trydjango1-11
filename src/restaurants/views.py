from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def home(request):
    context = {

    }
    return render(request, "home.html", context)


def about(request):
    context = {

    }
    return render(request, "about.html", context)


def contact(request):
    context = {

    }
    return render(request, "contact.html", context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)
