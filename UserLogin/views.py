from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import UserForm


def home(request):
    context = {}
    if request.user:
        context = {'logout': True}
    return render(request, 'home.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'home.html')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['username'] = username

                return redirect('UserLogin:profile')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})

    if request.session.has_key('username'):
        user = request.user
        print(user)
        return redirect('UserLogin:profile')

    return render(request, 'login.html')


def logout_user(request):
    try:
        del request.session['user']
    except:
        pass
    logout(request)
    form = UserForm(request.POST or None)

    return redirect('UserLogin:login_user')


def validate_data(request):
    username = request.GET.get('username', None)
    if username:
        data = {
            'notvalid': User.objects.filter(username__iexact=username).exists()
        }
        if data['notvalid']:
            data['error_message'] = 'A user with this username already exists.'
        return JsonResponse(data)
    else:
        password1 = request.GET.get('password1', None)
        password2 = request.GET.get('password2', None)
        data = {
            'notvalid': password1 != password2,
        }

        if data['notvalid']:
            data['error_message'] = 'password doesn`t match '
        return JsonResponse(data)


def profile(request):
    if request.session.has_key('username'):
        if request.user.is_authenticated:
            user = request.user
            return render(request, 'profile.html', {'user': user})
        else:
            return render(request, 'login.html')
    else:
        return redirect('UserLogin:login_user')
