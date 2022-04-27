from django.shortcuts import redirect, render,get_object_or_404
from .forms import Vote, VoteForm, CommentForm, Comment
from django.db.models import Count
import random
# Create your views here.
def index(request):
    votes = Vote.objects.order_by('-pk')
    one = random.sample(list(votes),1)[0]
    random_one = Vote.objects.get(title=one)
    context = {
        'votes':votes,
        'random_one':random_one
    }
    return render(request,'eithers/index.html',context)

def create(request):
    if request.method == 'POST':
        vote_form = VoteForm(request.POST)
        if vote_form.is_valid():
            vote_form.save()
            return redirect('eithers:index')
    else:
        vote_form = VoteForm()
    context = {
        'vote_form' : vote_form,
    }
    return render(request,'eithers/create.html',context)

def detail(request,pk):
    vote = get_object_or_404(Vote,pk=pk)
    comment_form = CommentForm()
    comments = vote.comment_set.all()
    length = int(Comment.objects.filter(vote_id=pk).aggregate(Count('pick'))['pick__count'])
    if length != 0:
        blue = int(Comment.objects.filter(vote_id=pk,pick='Blue').aggregate(Count('pick'))['pick__count'])/length*100
        red = int(Comment.objects.filter(vote_id=pk,pick='Red').aggregate(Count('pick'))['pick__count'])/length*100
    else:
        blue = 0
        red = 0
    context = {
        'vote':vote,
        'comment_form':comment_form,
        'comments':comments,
        'blue':blue,
        'red':red,
    }
    return render(request,'eithers/detail.html',context)

def comment_create(request,pk):
    vote = get_object_or_404(Vote,pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.vote = vote
        comment.save()
    return redirect('eithers:detail',pk)