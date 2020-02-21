# Tests on this page for correct location i.e url and the correct template

from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item

class TestViews(TestCase):
  def test_get_home_page(self):
    # built in helper (client.get) that will basically fake a request to the url that we pass in the argument (/)
    page = self.client.get('/')
    self.assertEqual(page.status_code, 200)
    self.assertTemplateUsed(page, 'todo_list.html')

  def test_get_add_item_page(self):
    page = self.client.get('/add')
    self.assertEqual(page.status_code, 200)
    self.assertTemplateUsed(page, 'item_form.html')

  def test_get_edit_item_page(self):
    item = Item(name='Create a Test')
    item.save()
    
    page = self.client.get('/edit/{0}'.format(item.id))
    self.assertEqual(page.status_code, 200)
    self.assertTemplateUsed(page, 'item_form.html')

# to test the above (test_get_edit_item_page) we need to pass through an ID 
      # so I'm gonna open my curly brace
      # pop in a zero and pop in a closing brace and I'm gonna use the format
      # method to pass in an ID here but in order to pass in an ID we must first have an
      # object in the database I mean we can't just pass in an ID because it will fail
      # because there's no objects in a database. So here im creating an instance of the item model."""
  
  def test_get_edit_page_for_item_that_does_not_exist(self):
    # no need to test template test because we have already done that, i.e. test_get_edit_item_page
   page = self.client.get('/edit/1')
   self.assertEqual(page.status_code, 404) 

  def test_post_create_an_item(self):
    # the url we are going to post to is '/add'
    # then we're going to
    # create a dictionary of items that we're gonna pass to that URL
    response = self.client.post('/add', {'name': 'Create a Test'})
    item = get_object_or_404(Item, pk=1)
    self.assertEqual(item.done, False)

  def test_post_edit_an_item(self):
    item = Item(name='Create a Test')
    item.save()
    # we will get the ID of that item and store it in a variable called ID 
    id = item.id

    response = self.client.post('/edit/{0}'.format(id), {'name': 'A different name'})
    item = get_object_or_404(Item, pk=id)

    self.assertEqual('A different name', item.name)

  def test_toggle_status(self):
    item = Item(name='Create a Test')
    item.save()
    id = item.id

    # post to the toggle url and we are going to pass in the id so django knows which 1 to toggle
    response = self.client.post('/toggle/{0}'.format(id))

    item = get_object_or_404(Item, pk=id)
    self.assertEqual(item.done, True)


