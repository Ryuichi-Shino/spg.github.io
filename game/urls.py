from django.urls import path
from . import views
import sys
sys.dont_write_bytecode = True

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
    path('templates/quiz6', views.move_to_quiz6, name='move_to_quiz6'),
    path('templates/quiz7', views.move_to_quiz7, name='move_to_quiz7'),
    path('templates/quiz8', views.move_to_quiz8, name='move_to_quiz8'),
    path('templates/quiz9', views.move_to_quiz9, name='move_to_quiz9'),
    path('templates/quiz10', views.move_to_quiz10, name='move_to_quiz10'),
    path('templates/result', views.move_to_result, name='move_to_result'),
    path('templates/g3result', views.move_to_g3result, name='move_to_g3result'),
]

