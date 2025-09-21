from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('categories/<int:cat_id>/', views.categories),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('career', views.career, name='career'),
=======
    path('categories/<int:cat_id>/', views.categories, name='categories'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('career/', views.career, name='career')
>>>>>>> fea1ddb08459080fe811979e2bf507e42621471a
]
