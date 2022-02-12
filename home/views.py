from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class Main(TemplateView):
	template_name = "home/index.html"

