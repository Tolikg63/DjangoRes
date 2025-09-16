from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


data_db = [
    {'name': 'Tolik', 'surname': 'Tserunyan',
        'age': 29, 'is_published': True, 'id': 1},
    {'name': 'Hasmik', 'surname': 'Mirzoyan',
        'age': 26, 'is_published': True, 'id': 2},
    {'name': 'Gago', 'surname': 'Harutyunyan',
        'age': 30, 'is_published': True, 'id': 3},
    {'name': 'Tatev', 'surname': 'Chaparyan',
        'age': 23, 'is_published': True, 'id': 4}
]

menu_list = [
    {'title': 'Contact', 'user_title': 'contact'},
    {'title': 'Career', 'user_title': 'career'}
]


def index(request):
    # t = render_to_string('index.html')
    # return HttpResponse(t)
    data = {
        'menu': menu_list,
        'users': data_db
    }
    return render(request, 'index.html', data)


menu = ['Burger', 'Pizza', 'Sushi', 'PhoBo']


def about(request):
    data = {
        'title': menu_list,
        'number': 10,
        'about': 'about'
    }
    return render(request, 'about.html', data)


def categories(request, cat_id):
    print(request.GET)
    return HttpResponse(f"<h1>Categories page, ID number is {cat_id}</h1>")


def show_post(request, post_id):
    return HttpResponse(f"Post number is {post_id}")


def contact(request):
    return HttpResponse('Welcome to Contact page!')


def career(request):
    return HttpResponse('Welcome to Career page!')