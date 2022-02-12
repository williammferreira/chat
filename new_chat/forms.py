from django import forms
# from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile

class UserChatsForm(forms.Form):
	Description = forms.CharField()
	Invites = forms.CharField()
	class Meta:
		model = User
		fields = ['Description', 'Invites']
