from django.shortcuts import render
from django.http import FileResponse, Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from documents import models, serializers

class GreetView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({"message":"Hello from documents!"})

class DocumentViewSet(ModelViewSet):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    
    @action(detail=True, methods=['get'], url_path='download')
    def download(self, request, pk=None):
        try:
            document = self.get_object()
            return FileResponse(document.file.open('rb'), as_attachment=True, filename= document.name)
        except models.Document.DoesNotExist:
            raise Http404("Document not found")