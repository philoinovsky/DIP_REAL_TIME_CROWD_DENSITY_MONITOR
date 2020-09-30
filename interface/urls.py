from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('help', views.help, name='help'),
    path('EEE', views.EEE, name='EEE'),
    path('tutorialrooms', views.tutorialrooms, name='tutorialrooms'),
    path('trplus', views.trplus, name='trplus'),
    path('api/plot/', views.apiplot, name='apiplot'),
    re_path(r'.*',views.error_404_view, name='error_404_view'),
]

