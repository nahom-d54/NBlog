from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required

def _login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		print(username,password)

		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			error_message = 'Wrong Username or Password'
	else:
		error_message = None

	if request.user.is_authenticated:
		return redirect('home')
	else:
		return render(request,'auth/login.html',{'error':error_message})

def sign_up(request):
	if request.method == 'POST':
		redirect('home')
	if request.user.is_authenticated:
		return redirect('home')
	else:
		return render(request,'auth/sign_up.html')
	
@login_required
def _logout(request):
	logout(request)
	return redirect('home')