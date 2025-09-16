from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    # t = render_to_string('index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Main page from the data'
    }
    return render(request, 'index.html', data)


menu = ['Burger', 'Pizza', 'Sushi', 'PhoBo']


def about(request):
    data = {
        'title': menu,
        'number': 10,
        'about': 'about'
    }
    return render(request, 'about.html', data)


def categories(request, cat_id):
    print(request.GET)
    return HttpResponse(f"<h1>Categories page, ID number is {cat_id}</h1>")
