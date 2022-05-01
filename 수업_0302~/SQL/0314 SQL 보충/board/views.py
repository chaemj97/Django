from django.shortcuts import redirect, render
from .models import BlogPosting
# Create your views here.
def new(request):
    return render(request,'board/new.html')

def create(request):
    blog_posting = BlogPosting()
    blog_posting.author = request.POST['author']
    blog_posting.title = request.POST['title']
    blog_posting.content = request.POST['content']
    blog_posting.save()
    return redirect('board:detail',blog_posting.pk)

def index(request):
    blog_postings = BlogPosting.objects.all()
    context = {
        'blgo_postings' : blog_postings
    }
    return render(request,'board/index.html',context)

def detail(request,pk):
    blog_posting = BlogPosting.objects.get(pk=pk)
    context = {
        'blgo_posting' : blog_posting
    }
    return render(request,'board/detail.html',context)

def edit(request,pk):
    blog_posting = BlogPosting.objects.get(pk=pk)
    context = {
        'blgo_posting' : blog_posting
    }
    return render(request,'board/edit.html',context)

def update(request,pk):
    blog_posting = BlogPosting.objects.get(pk=pk)
    blog_posting.author = request.POST['author']
    blog_posting.title = request.POST['title']
    blog_posting.content = request.POST['content']
    blog_posting.save()
    return redirect('board:detail',blog_posting.pk)

def delete(request,pk):
    blog_posting = BlogPosting.objects.get(pk=pk)
    blog_posting.delete()
    return redirect('board:index')
