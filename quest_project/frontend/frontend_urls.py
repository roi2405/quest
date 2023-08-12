from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('user-1', index),
    path('question-1', index)
]