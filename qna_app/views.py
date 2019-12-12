from django.shortcuts import render
from .models import QuestionModel,AnswerModel

# Create your views here.
def question(request):
    questions = QuestionModel.objects.all()
    return render(request, 'question.html', {'questions': questions})

def popular(request):
    popularqs = QuestionModel.objects.filter(q_votes__gt = 2)
    return render(request, 'popular.html', {'popularqs':popularqs})