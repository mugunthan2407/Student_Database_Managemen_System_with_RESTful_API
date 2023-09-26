from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from stureg.models import Stureg
from stureg.serializers import SturegSerializer

# Create your views here.

@api_view(['GET','POST','DELETE'])
def stu_list(request):
    if request.method == 'GET':
        stu_data =Stureg.objects.all()
        sname = request.GET.get('sname',None)
        if sname is not None:
            stu_data = stu_data.filter(sname__icontains=sname)
        stu_serializer = SturegSerializer(stu_data,many=True)
        return JsonResponse(stu_serializer.data,safe=False)
    
    elif request.method == 'POST':
        stu_data = JSONParser().parse(request)
        stu_serializer = SturegSerializer(data=stu_data)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return JsonResponse(stu_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(stu_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Stureg.objects.all().delete()
        return JsonResponse({'message':'{} datas were deleted successfully!'.format(count[0])},
                          status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','PUT','DELETE'])
def stu_details(request,pk):
    try: 
        stu = Stureg.objects.get(pk=pk)
    except Stureg.DoesNotExist: 
        return JsonResponse({'message': 'The Student detail is wrong'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        stu_serializer = SturegSerializer(stu)
        return JsonResponse(stu_serializer.data)
    
    elif request.method == 'PUT':
        stu_data = JSONParser().parse(request)
        stu_serializer = SturegSerializer(stu, data=stu_data)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return JsonResponse(stu_serializer.data)
        return JsonResponse(stu_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        stu.delete()
        return JsonResponse({'message':'student dedails deleted successfully!'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def stu_bloodgroup(request):
    stu_data = Stureg.objects.filter(sbg="O pos")
    if request.method == 'GET':
        stu_serializer = SturegSerializer(stu_data,many=True)
        return JsonResponse(stu_serializer.data,safe=False)
    

