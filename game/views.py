from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'game/index.html')

def move_to_gamepage(request):
    return render(request, 'game/gamepage.html')

def move_to_gamepage2(request):
    return render(request, 'game/gamepage2.html')

def move_to_gamepage3(request):
    return render(request, 'game/gamepage3.html')

def move_to_oputionpage(request):
    return render(request, 'game/opution.html')

