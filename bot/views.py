from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView, CreateView
from .models import Facebook 

def index(request):
    return render(request, 'index.html')

class Bot(View):
	def get(self, request, *args, **kwargs):
		facebook = Facebook.objects.all().reverse()[0]
		
		if self.request.GET['hub.verify_token'] == facebook.verify_token:
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')
		
		return HttpResponse('Error, invalid token')
