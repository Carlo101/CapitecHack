from django.shortcuts import render
from django.template import Context, loader

def index(request):
	return render(request, 'donor.html')
