from django.shortcuts import render

# Create your views here.

from django.core.urlresolvers import reverse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from contacts.models import Contact

from django import forms

from contacts.forms import ContactForm

#from django import forms


class ListContactView(ListView):
	model = Contact
	template_name = 'contact_list.html'


class CreateContactView(CreateView):
	model = Contact
	template_name = 'edit_contact.html'
	#fields= ['first_name', 'last_name', 'email']
	form_class= ContactForm

	def get_success_url(self):
		return reverse('contacts-list')

	def get_context_data(self,**kwargs):
		context= super(CreateContactView, self).get_context_data(**kwargs)
		context['action']=reverse('contacts-new')
		return context


class UpdateContactView(UpdateView):
	model = Contact
	template_name= 'edit_contact.html'
	#fields= ['first_name', 'last_name', 'email']
	form_class= ContactForm

	def get_success_url(self):
		return reverse('contacts-list')

	def get_contact_data(self, **kwargs):
		context=super(UpdateContactView,self).get_contact_data(**kwargs)
		context['action']= reverse('contacts-edit', kwargs={'pk':self.get_object().id})
		return context

class DeleteContactView(DeleteView):
	model= Contact
	template_name= 'delete_contact.html'
	fields= ['first_name', 'last_name', 'email']

	def get_success_url(self):
		return reverse('contacts-list')


class ContactView(DetailView):
    model = Contact
    template_name = 'contact.html'