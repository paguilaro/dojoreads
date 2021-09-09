from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('revision', views.revision), 
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout)
]
