from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from .forms import UserEditForm, UserSignUpForm
from django.contrib import messages

# Create your views here.
def main(request):
	if request.method == "POST":
		form = UserSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for { username }! Please Log In.')
			return redirect('client:home')
		# else:
		# 	return redirect('sign_up')
	else:
		form = UserSignUpForm()
	data = {
		'form': form,
	}
	return render(request, "registration/signup.html", data)

class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        data = {
            'auth_form': UserEditForm(instance=request.user),
        }
        return render(request, 'account/settings.html', data)
    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Account changed successfully!")
            return redirect('account:settings_view')