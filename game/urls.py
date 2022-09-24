from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('templates/', views.move_to_gamepage, name='move_to_gamepage'),
    path('templates2/', views.move_to_gamepage2, name='move_to_gamepage2'),
    path('templates3/', views.move_to_gamepage3, name='move_to_gamepage3'),
    path('smallindex/',views.move_to_smallindex, name='move_to_smallindex'),
    path('bigindex/',views.move_to_bigindex, name='move_to_bigindex'),
    path('option/',views.move_to_optionpage, name='move_to_optionpage'),
]

import sys
sys.dont_write_bytecode = True