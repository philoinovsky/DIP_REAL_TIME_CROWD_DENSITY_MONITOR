from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('help', views.help, name='help'),
    path('EEE', views.EEE, name='EEE'),
    re_path(r'.*',views.error_404_view, name='error_404_view'),
]

