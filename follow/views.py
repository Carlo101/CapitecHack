from django.shortcuts import render
from django.template import Context, loader

def index(request):
	return render(request, 'recipient.html')

def donor(request):
	return render(request, 'donor.html')

def recipient(request):
	return render(request, 'recipient.html')