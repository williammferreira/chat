from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class chats(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE)
	chatCreator = models.TextField()
	chatUsers = models.TextField()
	chatName = models.TextField()
	chatDateCreated = models.TextField()
	chatArea = models.TextField()
	locationUrl = models.TextField()
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
