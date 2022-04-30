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
    #Adding New topics
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
