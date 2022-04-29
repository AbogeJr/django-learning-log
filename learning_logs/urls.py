"""Defines url patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    #Topics page
    path('topics/', views.topics, name='topics'),
    #Individual Topic Page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
