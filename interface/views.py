from . import plot
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from . models import s2_1,s2_b1,s2_b2,s2_b3,s2_b4
from . serializers import s2_1_Serializer,s2_b1_Serializer,s2_b2_Serializer,s2_b3_Serializer,s2_b4_Serializer

def error_404_view(request, exception=None):
   return render(request,'interface/error.html')

def index(request):
    template = loader.get_template('interface/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('interface/contact.html')
    context = {}
    return HttpResponse(template.render(context, request))

def aboutUs(request):
    template = loader.get_template('interface/aboutUs.html')
    context = {}
    return HttpResponse(template.render(context, request))

def help(request):
    template = loader.get_template('interface/help.html')
    context = {}
    return HttpResponse(template.render(context, request))

def EEE(request):
    template = loader.get_template('interface/EEE.html')
    context = {}
    return HttpResponse(template.render(context, request))

def apiplot(request):
    return HttpResponse(plot.Layout(500,500))

def tutorialrooms(request):
    template = loader.get_template('interface/tutorialrooms.html')
    context = {}
    return HttpResponse(template.render(context, request))

def trplus(request):
    template = loader.get_template('interface/trplus.html')
    context = {}
    return HttpResponse(template.render(context, request))

@api_view(['GET'])
def s2_1_list(request):
    s2_1_l = s2_1.objects.all()
    serializers = s2_1_Serializer(s2_1_l, many = True)
    return JsonResponse(serializers.data,safe=False)

@api_view(['GET'])
def s2_b1_list(request):
    s2_b1_l = s2_b1.objects.all()
    serializers = s2_b1_Serializer(s2_b1_l, many = True)
    return JsonResponse(serializers.data,safe=False)

@api_view(['GET'])
def s2_b2_list(request):
    s2_b2_l = s2_b2.objects.all()
    serializers = s2_b2_Serializer(s2_b2_l, many = True)
    return JsonResponse(serializers.data,safe=False)

@api_view(['GET'])
def s2_b3_list(request):
    s2_b3_l = s2_b3.objects.all()
    serializers = s2_b3_Serializer(s2_b3_l, many = True)
    return JsonResponse(serializers.data,safe=False)

@api_view(['GET'])
def s2_b4_list(request):
    s2_b4_l = s2_b4.objects.all()
    serializers = s2_b4_Serializer(s2_b4_l, many = True)
    return JsonResponse(serializers.data,safe=False)

@api_view(['GET', 'PUT'])
def s2_1_detail(request, pk):
    try:
        s2_1_d = s2_1.objects.get(pk=pk)
    except s2_1.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = s2_1_Serializer(s2_1_d)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = s2_1_Serializer(s2_1_d, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def s2_b1_detail(request, pk):
    try:
        s2_b1_d = s2_b1.objects.get(pk=pk)
    except s2_b1.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = s2_b1_Serializer(s2_b1_d)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = s2_b1_Serializer(s2_b1_d, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def s2_b2_detail(request, pk):
    try:
        s2_b2_d = s2_b2.objects.get(pk=pk)
    except s2_b2.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = s2_b2_Serializer(s2_b2_d)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = s2_b2_Serializer(s2_b2_d, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def s2_b3_detail(request, pk):
    try:
        s2_b3_d = s2_b3.objects.get(pk=pk)
    except s2_b3.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = s2_b3_Serializer(s2_b3_d)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = s2_b3_Serializer(s2_b3_d, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def s2_b4_detail(request, pk):
    try:
        s2_b4_d = s2_b4.objects.get(pk=pk)
    except s2_b4.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = s2_b4_Serializer(s2_b4_d)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = s2_b4_Serializer(s2_b4_d, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)