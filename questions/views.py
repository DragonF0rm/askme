# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    #TODO создать список вопросов
    #TODO использовать пагинацию (класс Pagination)
    return render(request,"index.html")

#def new_questions(request):
    #questions = Question.object.all().order_by{'-created_at')
    #return render(requests, 'list_questions.html', {
       # 'questions': questions
   # })

#def question(request,pk):
    #question = Question.objects.get(pk=pk)
    #return render(request, 'question.html', {
        #'questions': questions
    #})                     
