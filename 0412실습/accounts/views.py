from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST,require_http_methods
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 회원가입 성공
            user = form.save() 
            # 자동 로그인하기
            auth_login(request,user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)

@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인 되어있으면 수행 X
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)

@ require_POST
def logout(request):
    # 로그인 해야만 로그아웃 가능
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')

@ require_POST
def delete(request):
    if request.user.is_authenticated:
        # 회원탈퇴
        request.user.delete()
        # 유저의 세션 데이터 삭제 - 로그아웃
        auth_logout(request)
    return redirect('articles:index')

@ login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        print(1)
        if form.is_valid():
            print(2)
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form
    }
    print(3)
    return render(request,'accounts/update.html',context)

@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            # 암호 변경 되어도 로그인 유지
            update_session_auth_hash(request,form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request,'accounts/change_password.html',context)