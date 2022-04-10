from enum import auto
from nturl2path import url2pathname
from telnetlib import STATUS
import uuid
from django.db import models

# Create your models here.

class Document(models.Model):
	def get_UUID4_hex():
		return uuid.uuid4().hex

	def __str__(self):
		return self.title

	PUBLISHED = 'published'
	DRAFT = 'draft'

	STATUS_CHOICES = (
		('published', 'Published'),
		('draft', 'Draft'),
	)

	status = models.CharField(choices=STATUS_CHOICES, max_length=50, default=DRAFT)
	title = models.CharField(max_length=50)
	slug = models.CharField(max_length=50)
	body = models.TextField()
	group = models.OneToOneField('Group', on_delete=models.CASCADE, related_name="document_children", null=True, blank=True, default=None)
	id = models.CharField(default=get_UUID4_hex, primary_key=True, editable=False, max_length=1000)

class Group(models.Model):
	def get_UUID4_hex():
		return uuid.uuid4().hex

	def __str__(self):
		return self.title
	

	title = models.CharField(max_length=50)
	slug = models.CharField(max_length=50)
	parent = models.OneToOneField('self', on_delete=models.CASCADE, related_name="group_children", null=True, blank=True, default=None)
	id = models.CharField(default=get_UUID4_hex, primary_key=True, editable=False, max_length=1000)