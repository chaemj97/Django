from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'articles/index.html')

def new(request):
    return render(request,'articles/new.html')

def create(request):
    return render(request,'articles/create.html')

def detail(request,pk):
    return render(request,'articles/detail.html')

def edit(request,pk):
    return render(request,'articles/edit.html')

def delete(request):
    return render(request,'articles/delete.html')