from django.shortcuts import render, HttpResponse, redirect
from .models import Item
from .forms import ItemForm

# u need a view to create a html file
# Create your views here.

# def say_hello(request):
#   return HttpResponse('Hello World')
  
def get_todo_list(request):
  results = Item.objects.all()
  return render(request, 'todo_list.html', {'items': results})

# when we fill in our form (item_form.html) without filling the following code from (if.request etc) nothing happens. for a object to be stored it needs to have a request.method

# Constructor of the item form:

def create_an_item(request):
  if request.method=="POST":
    form = ItemForm(request.POST, request.FILES)
    # django then will check if the form is valid
    if form.is_valid():
      form.save()
    # new instance of item model
    return redirect(get_todo_list)
  else:
    form = ItemForm()

  return render(request, 'item_form.html', {'form': form}) 
