from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForm()
    context ={
        'form': form
    }
    return render(request, 'core/index.html', context)

def content_request(request):
    form = ContentRequestForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContentRequestForm()
    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)



def terms(request):
    return render(request, 'core/terms.html')



def privacy(request):
    return render(request, 'core/privacy.html')

def article(request):
    return render(request, 'core/article.html')