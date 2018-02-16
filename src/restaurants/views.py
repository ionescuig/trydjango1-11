from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello")
    return render(request, "base.html", {"html_var": "context variable"})


def home2(request):
    return HttpResponse("Hello")
