from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSignUpForm
from django.contrib import messages

# Create your views here.
def main(request):
	if request.method == "POST":
		form = UserSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for { username }! Please Log In.')
			return redirect('main')
		# else:
		# 	return redirect('sign_up')
	else:
		form = UserSignUpForm()
	data = {
		'form': form,
	}
	return render(request, "sign_up/index.html", data)