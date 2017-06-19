from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from pprint import pprint
from watson import search as watson
from .models import Facebook, IA, UserFacebook 
from .forms import IAForm

import json, requests, random, re

def facebook_app():
	facebook = Facebook.objects.all().reverse()[0]
	return facebook

def index(request):
    return render(request, 'index.html')


class Question(View):
	def get(self, request, *args, **kwargs):
		form = IAForm()
		context = {'form':form, 'success':False}		
		return render(request, 'question.html', context)
	def post(self, request, *args, **kwargs):
		success = False
		form = IAForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			success = True
		form = IAForm()
		context = {'form':form, 'success':success}		
		return render(request, 'question.html', context)

def post_facebook_message(senderid, message):
	find = True
	answer = ''
	
	user_url = "https://graph.facebook.com/v2.9/%s"%senderid 	
	user_details = {'fields':'first_name','access_token':facebook_app().token}  
	user_details = requests.get(user_url, user_details).json()

	user , created = UserFacebook.objects.get_or_create(sender_id=senderid);
	search_results = watson.filter(IA.objects.filter(question__iexact=message), message, ranking=False)
	
	if len(search_results) == 1:
		answer = search_results[0].answer
	else:
		answer = "Você dizia..."
		search_results_question = watson.filter(IA, message, ranking=True)
		if search_results_question:
			for result in search_results_question:
				answer += "%s " %(result.question)
		else:
			find = False
			answer = "Não entendi muito bem o que você disse %s, contribua com perguntas e repostas acessando nosso Website" %(user_details['first_name'])
	if find:
		data = {'text':answer}
	else:
		data = {"attachment":{"type":"template","payload":{"template_type":"button","text":answer,"buttons":[{"type":"web_url","url":"https://catatibot.herokuapp.com/question/","title":"Show Website"}]}}}

	if not created:
		user.text = message
		user.save()

	post_url = 'https://graph.facebook.com/v2.9/me/messages?access_token=%s'%facebook_app().token
	msg = json.dumps({"recipient":{"id":senderid}, "message":data})
	status = requests.post(post_url, headers={"Content-Type": "application/json"},data=msg)

	
class Bot(View):
	def get(self, request, *args, **kwargs):		
		if self.request.GET['hub.verify_token'] == facebook_app().verify_token:
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		# Converts the text payload into a python dictionary
		request_message = json.loads(self.request.body.decode('utf-8'))
		pprint (request_message)
		for entry in request_message['entry']:
			for message in entry['messaging']:
				if 'message' in message:
					if facebook_app().recipient != message['sender']['id']:					
						post_facebook_message(message['sender']['id'], message['message']['text'])		
		return HttpResponse()  

