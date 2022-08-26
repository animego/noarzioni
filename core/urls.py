from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matsa', views.matsa, name='matsa'),
    path('hofesh-habitoi', views.hofesh, name='hofesh'),
    path('mador', views.mador, name='mador'),
    path('hiztarfut', views.signin, name='signin'),
    path('kesher', views.kesher, name='kesher'),
]
