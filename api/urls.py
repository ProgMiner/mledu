from django.urls import path
from .views import GetAnswer

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('data/', GetAnswer.as_view()),
]