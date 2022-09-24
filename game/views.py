from django.shortcuts import render
from django.http import HttpResponse
import random
import sqlite3

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




#number_of_question = Question.objects.all().count() # データベースに格納している問題数
#question_array = [] # 問題番号を格納する配列を生成
#for num in range(1,number_of_question + 1): 
    #question_array.append(num)  # 問題番号を格納

#def NextQuestion(request):
    #template_name = 'gamepage3.html'
    random.shuffle(question_array)  # 問題番号をシャッフル
    #set_number = question_array[0]  # 最初の問題番号を取得
    #context = {
        #'question_list': Question.objects.filter(question_number = set_number),
        #"question_number":set_number
    #}
    #return render(request,template_name,context)




