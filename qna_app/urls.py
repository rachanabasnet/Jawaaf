
from django.urls import path
from qna_app import views
app_name = 'qna'

urlpatterns = [
    path('read/', views.questionlist, name='read'),
    path('popular/', views.popular, name='popular'),
    path('add/', views.add_question, name='add'),
    path('update/<int:id>', views.update_question, name='update'),
    path('delete/<int:id>', views.delete_question, name='delete'),
    path('vote_qn/<int:id>', views.vote_question, name='vote_qn'),
    path('answer/<int:id>', views.answer, name='answer'),
    path('listview/', views.QuestionListViews.as_view(), name='qnlist'),
]
