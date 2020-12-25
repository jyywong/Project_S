from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.views.generic import ListView

# Create your views here.
def signup(request):
    template = 'signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, template, {'form': form})

