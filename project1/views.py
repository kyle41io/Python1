from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

# Create your views here.
def index(request):
   return render(request, 'pages/project1.html')
def contact(request):
   return render(request, 'pages/contact.html')
def error(request):
   return render(request, 'pages/error.html')
def register(request):
   form = RegistrationForm()
   if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
          
   return render(request, 'pages/register.html', {'form': form})
