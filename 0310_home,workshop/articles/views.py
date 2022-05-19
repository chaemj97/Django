from re import A
from django.shortcuts import redirect, render
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request,'articles/index.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:index')

def detail(request,pk):
    articles = Article.objects.get(pk=pk)
    context = {
        'articles' : articles
    }
    return render(request,'articles/detail.html',context)

def edit(request,pk):
    articles = Article.objects.get(pk=pk)
    context = {
        'articles' : articles
    }
    return render(request,'articles/edit.html',context)

def delete(request,pk):
    articles = Article.objects.get(pk=pk)
    articles.delete()
    return redirect('articles:index')

def update(request,pk):
    articles = Article.objects.get(pk=pk)
    articles.title = request.POST.get('title')
    articles.content = request.POST.get('content')
    articles.save()
    return redirect('articles:index')