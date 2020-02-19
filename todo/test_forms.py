from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):
  # define a methhod on this class. Also if you start with is_this_thing_on without test in front django wont find the class to test
  def test_is_this_thing_on(self):
    self.assertEqual(1, 1)
