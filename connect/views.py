from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

#creating starting page 


def index(request):
    return HttpResponse('hello world')

#lets perform crud operation 

def question_list(request):
    question = Question.objects.all()
    context = {
        'question' : question
    }
    return render(request, 'questionlist.html', context)
