from django.shortcuts import render
from .models import QuestionModel,AnswerModel

# Create your views here.
def question(request):
    questions = QuestionModel.objects.all()
    return render(request, 'question.html', {'questions': questions})
