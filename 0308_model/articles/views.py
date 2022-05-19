from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Article
# Create your views here.
def index(request):
    # 여기에서 DB의 게시글 데이터를 가져와야 합니다.
    # 최근글부터
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request,'articles/index.html',context)

# 사용자가 내용을 작성하기 위해 보여주는 양식
def new(request):
    return render(request,'articles/new.html')

# 사용자가 작성한 내용을 저장하면 됩니다.
def create(request):
    # 사용자가 보낸 데이터를 받아서 DB에 저장
    # save()
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:index')

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/detail.html',context)