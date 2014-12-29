from django.forms import widgets
from rest_framework import serializers
from blog.models import BlogEntry


class BlogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntry
        fields = ('id', 'title', 'body')