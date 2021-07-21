from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from rest_framework import viewsets
from accounts.forms import LoginForm, SignupFormProfile, SignupFormUser, UpdateFormUser
from accounts.models import Profile
from .serializers import ProfileSerializer


User = get_user_model()


def home(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = None
    return render(request, 'accounts/auth_stub.html', {'profile': profile})


class LoginUser(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


def signup(request):
    if request.method == 'POST':
        userform = SignupFormUser(request.POST)
        profileform = SignupFormProfile(request.POST)
        if userform.is_valid() and profileform.is_valid():
            # create db objects
            user = userform.save()
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            # login and redirects
            password = userform.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('home')
    else:
        userform = SignupFormUser()
        profileform = SignupFormProfile()
    return render(request, 'accounts/signup.html', {'title': _('Signup'), 'userform': userform, 'profileform': profileform})


@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        userform = UpdateFormUser(request.POST, instance=request.user)
        profileform = SignupFormProfile(
            request.POST, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            username = user.username
            password = user.password
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        userform = UpdateFormUser(instance=request.user)
        profileform = SignupFormProfile(instance=request.user.profile)
    return render(request, 'accounts/signup.html', {'title': _('Update'), 'userform': userform, 'profileform': profileform})


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
