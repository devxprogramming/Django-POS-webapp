from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    return redirect('login_user')