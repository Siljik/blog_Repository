from django.shortcuts import render
from django.http import HttpResponse
from.models import blogModel
import json
from blog.serializer import blogserializer
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.

@csrf_exempt
def AddPost(request):
    if request.method=='POST':
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serialize_check=blogserializer(data=recieved_data)
        if serialize_check.is_valid():
            serialize_check.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
        

@csrf_exempt
def SearchPost(request):
    if request.method=='POST':
        recieved_data=json.loads(request.body)
        getUserid = recieved_data['userid']
        data=list(blogModel.objects.filter(Q(userid__icontains=getUserid)).values())
        return HttpResponse(json.dumps(data))
    


@csrf_exempt
def ViewPost(request):
    bloglist=blogModel.objects.all()
    serialize_data=blogserializer(bloglist,many=True)  
    return HttpResponse(json.dumps(serialize_data.data))