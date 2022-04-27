from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.order_by('-pk')
        context = {
            'todos':todos
        }
        return render(request, 'todos/index.html', context)
    else:
        return redirect('accounts:login') 

def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)