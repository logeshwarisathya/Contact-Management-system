from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# Read
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

# Create
def add_contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'add.html', {'form': form})

# Update
def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form})

# Delete
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('/')