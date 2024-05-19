from django.shortcuts import render
from rest_framework import viewsets
from tasks.models import Task
from tasks.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description)
        return JsonResponse({'message': 'Task created successfully'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
