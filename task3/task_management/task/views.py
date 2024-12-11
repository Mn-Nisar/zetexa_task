from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import Task, User
from.serializers import taskSerializer

from rest_framework.views import APIView
import csv




class TaskViewSetAPI(APIView):

    def post(self, request):
        
        if request.method == 'POST':
            task_data = request.data

            serializer = taskSerializer(data=task_data)
            
            if serializer.is_valid():
                serializer.save()

                return Response({'message': 'Task created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        
        status = request.GET.get('status', None)
        tasks = Task.objects.filter(status=status)

        serializer = taskSerializer(tasks, many=True)

        return Response(serializer.data)

