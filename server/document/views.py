from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializers import DocumentSerializer
from .utils.text_extractor import TextExtractor

class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        uploaded_file = self.request.FILES.get('file')
        print(TextExtractor(uploaded_file).extract_text())
        serializer.save(user=self.request.user)
        
         