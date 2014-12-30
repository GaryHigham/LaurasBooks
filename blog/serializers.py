from django.forms import widgets
from rest_framework import serializers
from blog.models import BlogEntry
from django.contrib.auth.models import User


class BlogEntrySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = BlogEntry       
        fields = ('id', 'created', 'title', 'titleMuted', 'synopsys', 'teaserImage', 'body', 'author')

class UserSerializer(serializers.ModelSerializer):
    blog = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogEntry.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'blog')