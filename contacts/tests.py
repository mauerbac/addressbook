from django.test import TestCase

# Create your tests here.

from contacts.models import Contact

class ContactTest(TestCase):

	def test_str(self):
		contact= Contact(first_name='Matt', last_name='Auerbach')

		self.assertEquals(str(contact), 'Matt Auerbach')