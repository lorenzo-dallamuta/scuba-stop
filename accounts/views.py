from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from accounts.forms import LoginForm, SignupFormProfile, SignupFormUser
from accounts.models import Profile

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
    return render(request, 'accounts/signup.html', {'title': 'Signup', 'userform': userform, 'profileform': profileform})


def update(request):
    if request.method == 'POST':
        profileform = SignupFormProfile(
            request.POST, instance=request.user.profile)
        if profileform.is_valid():
            profileform.save()
            username = request.user.username
            password = request.user.password
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        profileform = SignupFormProfile(instance=request.user.profile)
    return render(request, 'accounts/signup.html', {'title': 'Update', 'profileform': profileform})
