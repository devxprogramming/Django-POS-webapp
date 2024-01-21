from typing import Any
from django.shortcuts import render, redirect

from store.models import Product, Sale


from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.models import User

from django.views.generic import DetailView

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

class UserProfileDetail(DetailView):
    model = User
    template_name = 'auth/user_profile.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'user_profile'
        context['product'] = Product.objects.all()
        context['sold_by'] = Sale.objects.filter(issued_by=self.request.user)
        return context