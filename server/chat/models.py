from django.db import models
from uuid import uuid4
from django.conf import settings
from document.models import Document

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"
    
    class Meta:
        indexes = [
            models.Index(fields=['user', 'document'])
        ]
        ordering = ['-created_at']
    

class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    is_assistant = models.BooleanField(default=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.chat.title} by {'Assistant' if self.is_assistant else 'User'} Message"
    
    class Meta:
        indexes = [
            models.Index(fields=['chat', 'is_assistant'])
        ]
        ordering = ['-created_at']