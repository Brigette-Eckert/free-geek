from django.shortcuts import render, HttpResponseRedirect

def home(request):
    return render(request, 'home.html')
