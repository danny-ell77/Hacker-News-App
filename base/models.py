from django.db import models


class Story(models.Model):
    story_id = models.SmallIntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    news_type = models.CharField(max_length=10)
    url = models.URLField(blank=True, null=True)
    is_hackernews = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date', '-modified_date']
        verbose_name_plural = "Stories"

    def __str__(self) -> str:
        return self.title
