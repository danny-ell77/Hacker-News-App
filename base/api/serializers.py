from rest_framework import serializers
from base.models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        exclude = ['story_id']
        extra_kwargs = {'id': {"read_only": True}}

    def create(self, validated_data):
        story = Story.objects.create(**validated_data)
        story.is_hackernews = False
        story.save()
        return story

    