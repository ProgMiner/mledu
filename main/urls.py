from django.urls import path
from . import views, views_2
from .views import Logs

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.week_2, name="week_2"),
    path('week_2', views.week_2, name="week_2"),
    path('week_3', views.week_3, name="week_3"),
    path('week_4', views.week_4, name="week_4"),
    path('week_4_1', views.week_4_1, name="week_4_1"),
    path('week_4_2', views.week_4_2, name="week_4_2"),
    path('logs', Logs.as_view()),
    path('week_5', views_2.week_5, name="week_5"),
    path('week_6', views_2.week_6, name="week_6"),

]