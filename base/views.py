from django.core import paginator
from django.db.models.query_utils import PathInfo
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Story
from .filters import StoryFilter

stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'


def index(request):
    stories = Story.objects.all()
    storyFilter = StoryFilter(request.GET, queryset=stories)
    stories = storyFilter.qs
    paginator = Paginator(stories, 10)

    page = request.GET.get('page')

    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    context = {'stories': stories, 'storyFilter': storyFilter}
    return render(request, 'index.html', context=context)
