from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from bot import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
]