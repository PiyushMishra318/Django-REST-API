from newapp.models import Snippets
from newapp.serializers import SnippetSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from newapp.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.renderers import TemplateHTMLRenderer
from newapp.models import Snippets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'snippet-list.html'
    def get(self, request, format=None):
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer()
        return Response({'serializer':serializer,'snippets':snippets})

    def post(self, request, format=None):
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer,'snippets':snippets})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'snippet-detail.html'

    def get(self, request, pk, format=None):
        snippet = get_object_or_404(Snippets, pk=pk)
        serializer = SnippetSerializer(snippet)
        return Response({'serializer': serializer, 'snippet': snippet})

    def post(self, request, pk, format=None):
        snippet = get_object_or_404(Snippets, pk=pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'snippet': snippet})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDelete(APIView):
    def post(self, request, pk, format=None):
        snippet = get_object_or_404(Snippets, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
