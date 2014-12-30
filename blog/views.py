from blog.models import BlogEntry
from blog.serializers import BlogEntrySerializer
from blog.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions

class BlogList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = BlogEntry.objects.all()
	serializer_class = BlogEntrySerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = BlogEntry.objects.all()
	serializer_class = BlogEntrySerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
