from django.contrib import admin
from django.urls import path
from .views import ChatView,ChatBotInfoView

urlpatterns = [
    path('chat/',ChatView.as_view()),
    path('chatbot/info/<str:access_code>/',ChatBotInfoView.as_view())
    
]
