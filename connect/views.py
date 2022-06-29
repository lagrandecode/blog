from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Question
from .forms import FormConnect

# Create your views here.

#creating starting page 



#lets perform crud operation 

def question_list(request):
    question = Question.objects.all()
    context = {
        'question' : question
    }
    return render(request, "questionlist.html", context)

# using the below function for retrieving 

def question_retrieve(request,pk):
    retrieve = Question.objects.get(id=pk)
    context = {
        "retrieve" : retrieve
    }
    return render(request, "retrieve.html", context)




# def question_create(request):
#     form = FormConnect()
#     context = {
#         "form" : form
#     }
#     return render(request, "create.html", context)


def question_create(request):
    form = FormConnect()
    if request.method == "POST":
        form = FormConnect(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form" : form
    }
    return render(request, "create.html", context)

#CREATING UPDATE 

def question_update(request,pk):
    retrieve = Question.objects.get(id=pk)
    form = FormConnect(instance=retrieve)
    if request.method == "POST":
        form = FormConnect(request.POST, instance=retrieve)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form" : form
    }
    return render(request, "update.html", context)
    