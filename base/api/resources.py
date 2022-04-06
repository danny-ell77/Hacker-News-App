from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import Story
from base.api.serializers import StorySerializer


class StoryList(APIView):

    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StorySerializer(data=request.data)
        is_valid = serializer.is_valid(raise_exception=True)
        if is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)

    
class StoryDetail(APIView):

    def get_object(self, id):
        try:
            story = Story.objects.get(pk=id)
            return story
        except Story.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        story = self.get_object(pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)

    def put(self, request, pk):
        story = self.get_object(pk)
        serializer = StorySerializer(story, data=request.data)
        if serializer.is_valid and not story.is_hackernews:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        story = self.get_object(pk)
        if not story.is_hacknews:
            story.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        data = {
            "error": "You cannot delete this Story"
        }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

