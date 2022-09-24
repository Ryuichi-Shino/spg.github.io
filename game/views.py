from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'game/index.html')

def move_to_smallindex(request):
    return render(request, 'game/smallindex.html')

def move_to_bigindex(request):
    return render(request, 'game/bigindex.html')

def move_to_gamepage(request):
    return render(request, 'game/gamepage.html')

def move_to_gamepage2(request):
    return render(request, 'game/gamepage2.html')

def move_to_gamepage3(request):
    return render(request, 'game/gamepage3.html')

def move_to_optionpage(request):
    return render(request, 'game/option.html')

import sys
sys.dont_write_bytecode = True

def move_to_quiz1(request):
    return render(request, 'game/quiz1.html')

def move_to_quiz2(request):
    return render(request, 'game/quiz2.html')

def move_to_quiz3(request):
    return render(request, 'game/quiz3.html')

def move_to_quiz4(request):
    return render(request, 'game/quiz4.html')

def move_to_quiz5(request):
    return render(request, 'game/quiz5.html')

def move_to_result(request):
    return render(request, 'game/result.html')



