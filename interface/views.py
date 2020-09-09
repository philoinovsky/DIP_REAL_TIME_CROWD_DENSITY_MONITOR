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

def aboutUs(request):
    template = loader.get_template('interface/aboutUs.html')
    context = {}
    return HttpResponse(template.render(context, request))

def details(request):
    template = loader.get_template('interface/details.html')
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

def awards(request):
    template = loader.get_template('interface/awards.html')
    context = {}
    return HttpResponse(template.render(context, request))