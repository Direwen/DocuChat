from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields = ['id', 'name', 'file', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']
        
    def validate_file(self, value):
        if value.size > 10 * 1024 * 1024:
            raise serializers.ValidationError('File size should not exceed 10MB.')
        
        if value.name.split(".")[-1].lower() not in ['pdf', 'docx', 'txt']:
            raise serializers.ValidationError("File type not supported. Only pdf, docx, txt files are allowed.")
        
        return value