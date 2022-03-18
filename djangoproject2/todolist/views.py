from django.shortcuts import render

from .models import Todolistt

# Create your views here.

def index(requests):
    todo_items = Todolistt.objects.order_by('id')
    context = {'todo_items': todo_items}
    return render(requests,'todolist/index.html',context)
