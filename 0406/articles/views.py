from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
# Create your views here.
# articles 관련 템플릿은 articles/templates/articles/에 저장
def index(request):
    # 메인페이지를 요청 했을 때 게시글 전체 목록 읽어오기
    article = Article.objects.all().order_by('-pk')
    context = {
        'articles' : article,
    }
    return render(request,'articles/index.html',context)

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request,'articles/new.html',context)

def create(request):
    # 요청으로부터 데이터 받아서
    # Model객체에 담아서
    # DB API 활용해서 DB에 저장
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title,content=content)
    # article.save()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        # return redirect('articles:create')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request,'articles/create.html',context)  

def detail(request,pk):
    article= Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request,'articles/detail.html',context)
    
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=article)
        # 수정 요청        
        if form.is_valid:
            form.save()
            return redirect('articles:detail',article.pk)
    else: # 수정 양식 요청
        form = ArticleForm(instance=article)
   
    context = {
        'form': form,
        'article': article
    }
    return render(request,'articles/update.html',context)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)