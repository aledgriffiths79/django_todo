from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestToDoItemForm(TestCase):
  # define a methhod on this class. Also if you start with is_this_thing_on without test in front django wont find the class to test
  def test_can_create_an_item_with_just_a_name(self):
    # instantiate this object using a dictionary
    form = ItemForm({'name': 'Create Tests'})
    self.assertTrue(form.is_valid())

  def test_correct_message_for_missing_name(self):
    form = ItemForm({'name': ''})
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['name'], [u'This field is required.'])

