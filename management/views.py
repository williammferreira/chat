from django.shortcuts import render
from django.views.generic import ListView
from .models import App

# Create your views here.


class AppListView(ListView):
    model = App
    template_name_suffix = "_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(users=self.request.user.profile)
