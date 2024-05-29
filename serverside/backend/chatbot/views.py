from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ChatView(APIView):
    def get(self, request, format=None):
        return Response({'status':'success'},status=status.HTTP_200_OK)
    
    def post(self,request):
        pass
    

class ChatBotInfoView(APIView):
    def get(self, request, access_code):
        return Response({'status':access_code},status=status.HTTP_200_OK)