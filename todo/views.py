from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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

def edit_an_item(request, id):
  # i want to get the object from the item model and the specific 1 i want is the primary key pk with value equal to the id. pk stands for primary key, it is like the ObjectId of a data entry in mongodb. A primary key is unique to a specific entry in the database.
  item = get_object_or_404(Item, pk=id)
  # saving the instance of this object. Creating a new instance of item, means adding a new entry to the database in the Item table.

  if request.method == 'POST':
    form = ItemForm(request.POST, instance=item)
    if form.is_valid():
      form.save()
      return redirect(get_todo_list)
  else:
    form = ItemForm(instance=item)

  return render(request, 'item_form.html', {'form': form}) 

  # doing a git pull experiment. why? i updated a readme file remotely i.e github but not locally. but then when i had features updated locally that i wanted to push remotely it wouldnt allow me too until i sorted the readme file. i then inputted in the cmd terminal git push origin master --force. it worked. But its a bad practice because when you use --force you override anything so everything you overwritten is lost. by pulling them then pushing is the correct way as you preserve history

def toggle_status(request, id):
  item = get_object_or_404(Item, pk=id)
  # always flip the opposite so if its not done then it will set it to done and if its done it will set it to it not done
  item.done = not item.done
  item.save()
  return redirect(get_todo_list)

