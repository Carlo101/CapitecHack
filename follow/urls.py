from django.urls import path
from . import views


urlpatterns =[
	path('', views.index, name='index'),
	path('/donor', views.index, name='donor'),
	path('/recipient', views.index, name='recipient')
]