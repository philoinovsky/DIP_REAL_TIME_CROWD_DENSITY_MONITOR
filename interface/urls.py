from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('details', views.details, name='details'),
    path('help', views.help, name='help'),
    path('EEE', views.EEE, name='EEE'),
    path('awards', views.awards, name='awards'),
]