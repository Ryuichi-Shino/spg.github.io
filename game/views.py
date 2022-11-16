from django.shortcuts import render
from django.http import HttpResponse
import sys
sys.dont_write_bytecode = True
from game.models import Score
from django.contrib import messages

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


def move_to_quiz1(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()
    score.reset()
    context = { 'score':score }
    return render(request, "game/quiz1.html", context)

def move_to_quiz2(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz2.html", context)
    
def move_to_quiz3(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz3.html", context)

def move_to_quiz4(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz4.html", context)

def move_to_quiz5(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz5.html", context)

def move_to_quiz6(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz6.html", context)

def move_to_quiz7(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz7.html", context)

def move_to_quiz8(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz8.html", context)

def move_to_quiz9(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz9.html", context)

def move_to_quiz10(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz10.html", context)



def move_to_result(request):
    try:
        score = Score.objects.get(pk=1)
    except Score.DoesNotExist:
        score = Score(score=0)
        score.save()

    if request.method=='POST':
        ans = request.POST['answer']
        if (ans == 'correct'):
            score.increment()
    context = { 'score':score }
    return render(request, "game/quiz_result.html", context)
