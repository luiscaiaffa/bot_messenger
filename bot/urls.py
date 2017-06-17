from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from bot import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^66d2b8f4a09cd35cb23076a1da5d51529136a3373fd570b122/?$', views.Bot.as_view(), name="bot") 
]