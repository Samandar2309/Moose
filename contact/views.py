from django.shortcuts import render
from .forms import ContactForm
from .models import Contact2


# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    posts = Contact2.objects.all().order_by('id')[:1]
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        'posts': posts,
    }
    return render(request, 'contact.html', context)


