from django.urls import path
from . import views

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.week_2, name="week_2"),
    path('week_2', views.week_2, name="week_2"),
    path('week_3', views.week_3, name="week_3"),
]