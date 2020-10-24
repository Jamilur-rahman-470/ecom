from core.models import AddressAndInfo, Profile
from core.decorators import address_exists, allowed_user, authenticated_user, profile_exists
from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserProfileForm, AddressForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.


# LOGIN USER
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


# REGISTER USER
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


# USER DASHBOARD
@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def user_dashboard(request):
    is_there = Profile.objects.filter(user = request.user)
    address_there = AddressAndInfo.objects.filter(user = request.user)

    profile = None
    address = None
    if (address_there):
        address = AddressAndInfo.objects.get(user = request.user)
    else: 
        address = None

    if is_there:
        profile = Profile.objects.get(user = request.user)
    else:
        profile = None
    context = {
        'profile': profile,
        'have_profile': is_there,
        'address_there': address_there,
        'address': address
    }
    return render(request, 'core/user_dash.html', context)


# UPDATE USER PROFILE
@profile_exists
@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def profile_update(request):
    profile_form = UserProfileForm()
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save(request.user)
            messages.success(request, 'PROFILE UPDATED')
            return redirect('dash')
    context = {
        'profile_form': profile_form
    }
    return render(request, 'core/profile_update.html', context)


# ADD ADDRESS
@address_exists
@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def address_update(request):
    address_form = AddressForm()
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address_form.save(request.user)
            messages.success(request, 'address UPDATED')
            return redirect('dash')
    context = {
        'address_form': address_form
    }
    return render(request, 'core/address_update.html', context)



# LOGOUT USER
def logout_user(request):
    logout(request)
    return redirect('login')
