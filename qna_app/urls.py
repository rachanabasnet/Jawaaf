
from django.urls import path
from .views import question,popular

urlpatterns = [
    path('question/', question),
    path('popular/', popular),
]
