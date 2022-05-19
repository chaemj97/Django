from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 전체 게시글 조회(오름차순)
    # articles = Article.objects.all()

    # 전체 게시글 조회(내림차순 1, python으로 조작)
    # articles = Article.objects.all()[::-1]
    
    # 전체 게시글 조회(내림차순 2, DB가 조작)
    articles = Article.objects.order_by('-pk')

    # 조회해서 할당한 쿼리셋 데이터를 context로 넘김
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return redirect('/articles/')
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    # print(request.method)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
