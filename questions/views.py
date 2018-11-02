# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def hello(request):
    return render(request,"list_questions.html")

#def new_questions(request):
    #TODO использовать пагинацию (класс Pagination)
    #questions = Question.object.all().order_by{'-created_at')
    #return render(requests, 'list_questions.html', {
       # 'questions': questions
   # })

#def question(request,pk):
    #question = Question.objects.get(pk=pk)
    #return render(request, 'question.html', {
        #'questions': questions
    #})
~                     
