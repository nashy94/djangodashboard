from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messgaes.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=pass1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request, 'User Created')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not Match')
            return redirect('register')
    else:
        return render(request, 'register.html', {})


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username=username,password=pass1)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username and or Password')
            return redirect('login')
    else:
        return render(request, "login.html", {})