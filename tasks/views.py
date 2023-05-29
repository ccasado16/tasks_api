from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from tasks.models import Task
from tasks.serializers import TaskSerializer
from django.http import JsonResponse,  HttpResponse
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def tasks(request):
    """List all tasks"""
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return JsonResponse(serializer.data, safe=False)
    
    """Create a new task"""
    elif (request.method =="POST"):
        # parse the incoming information to django
        data = JSONParser().parse(request)

        serializer = TaskSerializer(data=data)

        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, pk):
    try: 
        task = Task.objects.get(pk=pk)
    except: 
        return HttpResponse(status=404)

    if (request.method == "PUT"):
        # parse the incoming information
        data = JSONParser().parse(request)

        serializer = TaskSerializer(task, data=data)

        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        
        return JsonResponse(serializer.errors, status=400)
    
    elif (request.method == "DELETE"):
        task.delete()
        return HttpResponse(status=204)
        