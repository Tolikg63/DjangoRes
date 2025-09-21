from django.http import HttpResponse
from django.shortcuts import render


menu_list = [
    {'name': 'About', 'url_name': 'about'},
    {'name': 'Contacts', 'url_name': 'contacts'},
    {'name': 'Career', 'url_name': 'career'},
]


def index(request):
    data = {
        'menu': menu_list
    }
    return render(request, 'index.html', context=data)


def categories(request, cat_id):
    return HttpResponse(f"<h1>Categories page, It is the {cat_id} category</h1>")



def about(request):
    return render(request, 'about.html')


def contacts(request):
    data = {
        'menu': menu_list
    }
    return render(request, 'contacts.html', context=data)


def career(request):
    return render(request, 'career.html')
