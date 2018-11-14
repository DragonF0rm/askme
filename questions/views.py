# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Question


def index(request):
    #TODO использовать пагинацию (класс Pagination)
    question_list = Question.objects.order_by('-created_at')
    return render(request, 'index.html', {'question_list': question_list})


def one_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    return render(request, 'one_question.html', {'question': question})
