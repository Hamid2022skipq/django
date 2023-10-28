import io
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import StudentSerializers
from .models import Student

def serialization(request,pk):
    # stu=Student.objects.get(id=2)
    # stu=Student.objects.all()
    stu=Student.objects.get(id=pk)
    serial=StudentSerializers(stu)
    # serial=StudentSerializers(stu,many=True)
    json_data=JSONRenderer().render(serial.data)
    return HttpResponse(json_data,content_type='application/JSON')
    # return render(request,'hello.html',{'json_data':json_data})

def studentinfo(request):
    stu=Student.objects.all()
    serail=StudentSerializers(stu,many=True)
    json_data=JSONRenderer().render(serail.data)
    return HttpResponse(json_data,content_type='application/JSON')
@csrf_exempt
def StudentCreate(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializate=StudentSerializers(data=python_data)
        if serializate.is_valid():
            serializate.save()
            msg = {'msg': 'Data inserted Successfully'}
            return JsonResponse(msg)
        # json_data=JSONRenderer().render(serializate.errors)
        # return HttpResponse(json_data,content_type='application/JSON')
        return JsonResponse(serializate.errors, status=400)
    
@csrf_exempt
def StudentUpdate(request):
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        serializate=StudentSerializers(data=python_data)
        if serializate.is_valid():
            serializate.save()
            msg = {'msg': 'Data updated Successfully'}
            return JsonResponse(msg)
        # json_data=JSONRenderer().render(serializate.errors)
        # return HttpResponse(json_data,content_type='application/JSON')
        return JsonResponse(serializate.errors, status=400)