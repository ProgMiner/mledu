from django.urls import path

from . import views, views_2

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', views.week_2, name="week_2"),
    path('week_2', views.week_2, name="week_2"),
    path('week_3', views.week_3, name="week_3"),
    path('week_4', views.week_4, name="week_4"),
    path('week_4_1', views.week_4_1, name="week_4_1"),
    path('week_4_2', views.week_4_2, name="week_4_2"),
    path('week_5', views_2.week_5, name="week_5"),
    path('week_61', views_2.week_61, name="week_61"),
    path('week_62', views_2.week_62, name="week_62"),
    path('week_7', views_2.week_7, name="week_7"),
    path('week_81', views_2.week_81, name="week_81"),
    path('week_82', views_2.week_82, name="week_82"),
    path('week_9', views_2.week_9, name="week_9"),
    path('week_10', views_2.week_10, name="week_10"),
    path('week_11', views_2.week_11, name="week_11"),
    path('week_12', views_2.week_12, name="week_12"),
    path('week_12_ping', views_2.week_12_ping, name="week_12_ping"),
]
