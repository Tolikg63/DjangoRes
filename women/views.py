from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


data_db = [
    {'name': 'Tolik', 'surname': 'Tserunyan', 'age': 29, 'is_published': False},
    {'name': 'Hasmik', 'surname': 'Mirzoyan', 'age': 26, 'is_published': True},
    {'name': 'Gago', 'surname': 'Harutyunyan', 'age': 30, 'is_published': True},
    {'name': 'Tatev', 'surname': 'Chaparyan', 'age': 23, 'is_published': True}
]


def index(request):
    # t = render_to_string('index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Main page from the data',
        'users': data_db
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
