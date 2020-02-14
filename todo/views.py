from django.shortcuts import render, HttpResponse, redirect
from .models import Item

# u need a view to create a html file
# Create your views here.

# def say_hello(request):
#   return HttpResponse('Hello World')
  
def get_todo_list(request):
  results = Item.objects.all()
  return render(request, 'todo_list.html', {'items': results})

# when we fill in our form (item_form.html) without filling the following code from line 16 (if.request etc to line 25) nothing happens. for a object to be stored it needs to have a request.method
def create_an_item(request):
  if request.method=="POST":
    # new instance of item model
    new_item = Item()
    new_item.name = request.POST.get('name')
    # FOR A line in name object i.e aled(line through middle of name) you must input the following:
    new_item.done = 'done' in request.POST
    new_item.save()

    return redirect(get_todo_list)

  return render(request, 'item_form.html') 
