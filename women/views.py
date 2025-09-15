from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    t = render_to_string('index.html')
    return HttpResponse(t)


def categories(request, cat_id):
    print(request.GET)
    return HttpResponse(f"<h1>Categories page, ID number is {cat_id}</h1>")