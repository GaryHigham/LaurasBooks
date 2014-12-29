from blog.models import BlogEntry
from blog.serializers import BlogEntrySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BlogList(APIView):
	queryset = BlogEntry.objects.all()

	def get(self, request, format=None):
	    entries = self.queryset
	    serializer = BlogEntrySerializer(entries, many=True)
	    return Response(serializer.data)

	def post(self, request, format=None):
	    serializer = BlogEntrySerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data, status=status.HTTP_201_CREATED)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(APIView):
	queryset = BlogEntry.objects.all()

	def get_object(self, pk):
	    try:
	        return self.queryset.get(pk=pk)
	    except BlogEntry.DoesNotExist:
	        raise Http404

	def get(self, request, pk, format=None):
	    entry = self.get_object(pk)
	    serializer = BlogEntrySerializer(entry)
	    return Response(serializer.data)

	def put(self, request, pk, format=None):
	    entry = self.get_object(pk)
	    serializer = BlogEntrySerializer(entry, data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
	    entry = self.get_object(pk)
	    entry.delete()
	    return Response(status=status.HTTP_204_NO_CONTENT)
