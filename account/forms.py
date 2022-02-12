from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import Profile

class UserSignUpForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField()
	helper = FormHelper()
	helper.form_show_labels = False
	last_name = forms.CharField()
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']