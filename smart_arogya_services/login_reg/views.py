from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
# Create your views here.

def login(request):

    if request.method == 'POST':
        uname = request.POST['UserName']
        password = request.POST['Password']

        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('register')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    elif request.method == 'GET':
        return render(request, 'Login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['Name']
        uname = request.POST['UserName']
        email = request.POST['Email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']

        if password1 == password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=name, username=uname, email=email, password=password1,)
                user.save()
                messages.info(request, 'user created')
                return redirect('login')
        else:
            messages.info(request, 'password not macthcing..')
            return redirect('register')

    elif request.method == 'GET':
        return render(request, 'RegisterForm.html')
