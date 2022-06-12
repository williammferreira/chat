from django.shortcuts import render
from django.views.generic import ListView
from management.models import App

# Create your views here.


class AppListView(ListView):
    model = App
    template_name = "store/store.html"
