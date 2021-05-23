from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class chats(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE)
	chat_creator = models.TextField()
	chat_users = models.TextField()
	chat_name = models.TextField()
	chat_date_created = models.TextField()
	chat_area = models.TextField()
	location_url = models.TextField()
	token = models.TextField(primary_key=True)
	# def __str__(self):
	# 	return f"""[
	# 	{ self.chat_name },
	# 	{ self.chat_creator },
	# 	{ self.chat_users },
	# 	{ self.chat_date_created },
	# 	{ self.chat_area },
	# 	{ self.location_url }
	# 	]""" #f"{ self.user.username } Chats"
