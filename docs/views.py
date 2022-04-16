from django.shortcuts import render
from django.views.generic import View, ListView
from django.core import serializers
from .models import Group, Document

# Create your views here.

class DocumentView(View):
	def get(self, request, raw_url):
		url = raw_url.split('/')
		url.remove('') if url[-1] == '' else 0
		print(url)
		for i in url:
			if i is not url[-1]:
				try:
					Group.objects.get(slug=i)
				except Group.DoesNotExist:
					return render(request, 'docs/doc_not_found.html', {
						'url': raw_url,
					})
			else:
				try:
					doc = Document.objects.get(slug=i)
					print(i)
					return render(request, 'docs/document.html', {
						'type': 'document',
						'document': doc,
					})
				except Document.DoesNotExist:
					try:
						group = Group.objects.get(slug=i)
						print("wow")
						return render(request, 'docs/document.html', {
							'type': 'group',
							'group': group,
						})
					except Group.DoesNotExist:
						pass
		return render(request, 'docs/doc_not_found.html', {
			'url': raw_url,
		})

class StartView(View):
	def get(self, request):
		queryset = Group.objects.all()
		print(queryset)
		json_queryset = serializers.serialize('json', queryset)

		return render(request, 'docs/start.html', {
			'groups': queryset,
		})