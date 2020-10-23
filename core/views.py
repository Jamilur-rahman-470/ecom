from core.decorators import allowed_user, authenticated_user
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.

@authenticated_user
def login_user(request):

    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if(user is not None):
            login(request, user)
            return redirect('dash')
        else:
            messages.error(request, 'username or password wrong')
    return render(request, 'core/login.html')

@authenticated_user
def register_user(request):
    form = CreateUserForm()
    if (request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Registration Successful')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'core/register.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def user_dashboard(request):
    return render(request, 'core/user_dash.html')


def logout_user(request):
    logout(request)
    return redirect('login')
