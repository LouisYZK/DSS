from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
# Create your views here.
def index(request):
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)	
def heello(request):
	pass