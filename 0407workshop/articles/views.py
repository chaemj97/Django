from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    article = Article.objects.all().order_by('-pk')
    context = {
        'articles':article
    }
    return render(request,'articles/index.html',context)

def create(request):
    # POST : 데이터 베이스에 조작을 가함 : create : 새글 쓰기 요청
    # GET : 데이터를 조회만 함 : new : 새글 쓰기 위한 양식 요청
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request,'articles/create.html',context)

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request,'articles/detail.html',context)

def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST': # update
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else: # edit
        form = ArticleForm(instance=article)
    context = {
        'article':article,
        'form':form
    }
    return render(request,'articles/update.html',context)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)