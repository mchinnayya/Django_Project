from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import random
import json

def home(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')  # Use mobile number instead of username
        password = request.POST.get('password')
        user = authenticate(request, username=mobile, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login successful!')
        else:
            return HttpResponse('Invalid credentials, please try again.')
    return render(request, 'login.html')

def forgot_password(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        try:
            user = User.objects.get(username=mobile)
            # Generate a temporary password
            temp_password = str(random.randint(100000, 999999))
            user.set_password(temp_password)
            user.save()
            return JsonResponse({'message': f'Temporary password sent to your mobile: {temp_password}'})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Mobile number not registered.'})
    return render(request, 'forgot_password.html')

def sign_up(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            mobile = data.get('mobile')
            password = data.get('password')
        else:
            mobile = request.POST.get('mobile')
            password = request.POST.get('password')
        if not password:
            return JsonResponse({'error': 'Password field is required.'})
        if len(password) < 4:
            return HttpResponse('Password must be at least 4 characters long.')
        if User.objects.filter(username=mobile).exists():
            return HttpResponse('Mobile number already registered.')
        else:
            user = User.objects.create_user(username=mobile, password=password)
            user.save()
            return HttpResponse('Sign up successful! Redirecting to login...')
            return redirect('/')
    return render(request, 'sign_up.html')

