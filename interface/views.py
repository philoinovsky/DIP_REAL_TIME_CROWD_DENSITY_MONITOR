from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('interface/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('interface/contact.html')
    context = {}
    return HttpResponse(template.render(context, request))