# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Question


def index(request):
    #TODO использовать пагинацию (класс Pagination)
    question_list = Question.objects.order_by('-created_at')
    return render(request, 'index.html', {'question_list': question_list})

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
