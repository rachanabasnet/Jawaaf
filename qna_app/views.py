from django.shortcuts import render,redirect
from .models import QuestionModel,AnswerModel,CategoryModel
from .forms import QuestionForm,AnswerForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView

# Create your views here.

class QuestionListViews(ListView):
    queryset = QuestionModel.objects.all()


def questionlist(request):
    questionslist = QuestionModel.objects.all()
    return render(request, 'questionmodel_list.html', {'questionslist': questionslist})

def popular(request):
    popularqs = QuestionModel.objects.filter(q_votes__gt = 2)
    return render(request, 'popular.html', {'popularqs':popularqs})

def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid!')
    else:
        #form = QuestionForm
        category = CategoryModel.objects.all()
        return render(request, 'questionmodel_create.html', {'categories':category})

def update_question(request, id):
    question = QuestionModel.objects.get(id=id)
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid!')
    else:
        form = QuestionForm(instance=question)
        return render(request, 'questionmodel_update.html', {'form':form})

def delete_question(request, id):
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')

def vote_question(request, id):
    question = QuestionModel.objects.get(id=id)
    question.q_votes += 1
    question.save()
    return redirect('qna:read')

def answer(request, id):
    if request.method == "POST":
        answeredby = request.POST.get('ans_by')
        desc = request.POST.get('a_desc')
        image = request.POST.get('a_img')
        question = QuestionModel.objects.get(id=id)  
        Answer = AnswerModel(ans_by= answeredby, a_desc= desc, a_img= image, questions=question)
        Answer.save()
        return HttpResponse("Success")
    else:
        form = AnswerForm 
        a = {'form':form} 
        b = {'id':id}
        c = {**a, **b}
        return render(request, 'answermodel_create.html', c)
    