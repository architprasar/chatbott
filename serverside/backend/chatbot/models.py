from django.db import models
from django.contrib.auth.models import User
class ChatBot(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_code = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    company = models.CharField(max_length=255)
    company_logo = models.CharField(max_length=255)
    company_url = models.CharField(max_length=255)
    is_generated = models.BooleanField(default=False)
    llm_model = models.CharField(max_length=255)
    is_rag = models.BooleanField(default=False)
    has_functions = models.BooleanField(default=False)
    rag_dir = models.CharField(max_length=255)
    
    
    

class Message(models.Model):
    chatbot = models.ForeignKey(ChatBot, on_delete=models.CASCADE)
    message = models.TextField(blank=False)
    response = models.TextField(blank=True)
    origin_info = models.TextField(blank=True)
    