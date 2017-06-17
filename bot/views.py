from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from pprint import pprint
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

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		# Converts the text payload into a python dictionary
		incoming_message = json.loads(self.request.body.decode('utf-8'))
		pprint (incoming_message)

