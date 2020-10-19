from django.urls import path, re_path
from . import views
from rest_framework.authtoken import views as views_aut


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('help', views.help, name='help'),
    path('EEE', views.EEE, name='EEE'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('tutorialrooms', views.tutorialrooms, name='tutorialrooms'),
    path('trplus', views.trplus, name='trplus'),
    path('api/plot/', views.apiplot, name='apiplot'),
    path('s2_1', views.s2_1_list),
    path('s2_b1', views.s2_b1_list),
    path('s2_b2', views.s2_b2_list),
    path('s2_b3', views.s2_b3_list),
    path('s2_b4', views.s2_b4_list),
    path('s2_1/<int:pk>', views.s2_1_detail),
    path('s2_b1/<int:pk>', views.s2_b1_detail),
    path('s2_b2/<int:pk>', views.s2_b2_detail),
    path('s2_b3/<int:pk>', views.s2_b3_detail),
    path('s2_b4/<int:pk>', views.s2_b4_detail),
    path('api-token-auth/', views_aut.obtain_auth_token, name='api-token-auth'),
    re_path(r'.*', views.error_404_view, name='error_404_view'),
]
