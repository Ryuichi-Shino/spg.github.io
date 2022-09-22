from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('templates/', views.move_to_gamepage, name='move_to_gamepage'),
    path('templates2/', views.move_to_gamepage2, name='move_to_gamepage2'),
    path('templates3/', views.move_to_gamepage3, name='move_to_gamepage3'),
]