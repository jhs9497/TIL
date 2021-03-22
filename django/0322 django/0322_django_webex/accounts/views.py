from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login  # 장고의 login 함수를 불러와서 적용
from django.contrib.auth import logout as auth_logout  # 마찬가지
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm


# Create your views here.
def login(request):
    # if request.user.is_athenticated:
    #     # 로그인이 되어있다면.. 메인으로 리다이렉트!
    #     return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 이 시점에서 로그인...
            # 첫번째 인자에 요청 정보 (request)
            # 두번째 인자에 유저 객체 (..?)
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        # GET 요청일 때
        # 로그인 폼이 담긴 페이지를 보여줍니다.
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    # 로그아웃 == 세션을 삭제합니다.
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # 데이터베이스에 회원 정보 생성
            auth_login(request, user)
            return redirect('articles:index')
    else:
        # GET
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    # request.user == 여기까지가 현재 로그인 된 유저 객체

    # 실제 계정 삭제 대신 비활성화하는 경우
    # request.user.is_active = False
    # request.user.save()

    request.user.delete()
    return redirect('articles:index')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
