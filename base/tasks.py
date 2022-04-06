import requests
from base.models import Story
from celery import shared_task

stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

def get_stories(story_id):
    return requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json").json()


@shared_task
def sync_stories():
    resp = requests.get(stories_url).json()[:101]
    hackerrank_news = [get_stories(story_id) for story_id in resp]
    for item in hackerrank_news:
        story, created = Story.objects.get_or_create(story_id=item["id"])
        if created:
            story.title = item['title']
            story.author = item['by']
            if "text" in item.keys(): story.text = item['text']
            story.news_type = item['type']
            if "url" in item.keys(): story.url = item['url']
            story.save()
    print(Story.objects.last())