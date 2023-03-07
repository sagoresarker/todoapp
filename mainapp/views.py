from django.shortcuts import render, redirect, get_object_or_404
from django.core.cache import cache
from .models import Todo
from .forms import TodoForm
from todoapp.settings import CACHE_TTL
# Create your views here.

def index(request):

    todo_list = cache.get('todo_list')

    if not todo_list:
        todo_list = Todo.objects.all()
        cache.set('todo_list', todo_list, CACHE_TTL)

    print(todo_list)
    return render(request, 'mainapp/index.html', {'todo_list': todo_list})


def create_todo(request):
    form = TodoForm(request.POST or None)

    if request.method=='POST':
        if form.is_valid():
            form.save()

            return redirect('index')

    return render(request, 'mainapp/create_todo.html', {'form':form})


def update_todo(request, pk):
    selecte_todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=selecte_todo)
    if form.is_valid():
        form.save()

        return redirect('index')

    return render(request, 'mainapp/update.html', {'form':form})


def delete_todo(request, pk):
    selecte_todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        selecte_todo.delete()

        return redirect('index')
    
    return render(request, 'mainapp/delete_todo.html', {'selecte_todo':selecte_todo})

