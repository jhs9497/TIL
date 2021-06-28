from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib import messages
from .forms import CustomUserCreationForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # DB에 생성된 유저 객체 반환
            auth_login(request, user) # 로그인 == 세션 생성
            # 회원가입 축하 메세지(message)를 
            # request 객체에 담아서 같이 보냅니다.
            messages.add_message(
                request, messages.SUCCESS, '회원가입을 축하합니다!'
            )
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 세션 생성 (== 로그인)
            # 1. DB에 세션을 생성
            # 2. request 객체에 session 정보가 생성
            #    => request.session 사용 가능
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request) 
    # 세션 삭제 
    # 1. DB에 있는 세션 삭제
    # 2. request 객체에 담긴 session 삭제 
    return redirect('articles:index')


def update(request):
    from .forms import CustomUserChangeForm
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def password_update(request):
    from django.contrib.auth import update_session_auth_hash

    if request.method == 'POST':
        form = PasswordChangeForm(
            user=request.user, data=request.POST
        )
        if form.is_valid():
            form.save() # 비밀번호가 변경
            # form.get_user()
            auth_login(request, form.get_user())
            # update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password_update.html', context)