from django.shortcuts import render, redirect

import learning_logs
from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    """Home Page for Learning logs"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    "Show Topics"
    topics = Topic.objects.order_by('time_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    "Show individual topic with entry"
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a New Topic"""
    if request.method != 'POST':
        #No data submitted. Creating new form
        form = TopicForm()
    else:
        #Data submitted for processing
        form = TopicForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('learning_logs: topics')        

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

