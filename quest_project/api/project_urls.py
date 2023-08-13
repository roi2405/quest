from django.urls import path
from .views import CreateUserView, UserView


urlpatterns = [
    path('', UserView.as_view()),
    path('create-user', CreateUserView.as_view())
]
