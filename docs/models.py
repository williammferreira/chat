from django.db import models

# Create your models here.

class Document(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	slug = models.CharField(max_length=50)
	content = models.TextField()
	group = models.OneToOneField('Group', on_delete=models.CASCADE, null=True, blank=True, default=None)

class Group(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	slug = models.CharField(max_length=50)
	parent = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True, default=None)