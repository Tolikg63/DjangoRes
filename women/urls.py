from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<int:cat_id>/', views.categories),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('career', views.career, name='career'),
]
