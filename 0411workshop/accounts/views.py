from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users':users
    }
    return render(request, 'accounts/index.html',context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)