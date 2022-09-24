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
    path('templates/quiz1', views.move_to_quiz1, name='move_to_quiz1'),
    path('templates/quiz2', views.move_to_quiz2, name='move_to_quiz2'),
    path('templates/quiz3', views.move_to_quiz3, name='move_to_quiz3'),
    path('templates/quiz4', views.move_to_quiz4, name='move_to_quiz4'),
    path('templates/quiz5', views.move_to_quiz5, name='move_to_quiz5'),
    path('templates/result', views.move_to_result, name='move_to_result'),
]

import sys
sys.dont_write_bytecode = True