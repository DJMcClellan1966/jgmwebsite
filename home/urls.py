from django.urls import path, include
from . import views


urlpatterns = [
    path('terms', views.terms, name = 'terms'),
    path('privacy', views.privacy, name = 'privacy'),
    path('home', views.home, name = 'home'),

    ]
