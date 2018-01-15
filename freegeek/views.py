from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import json

def home(request):
    return render(request, 'home.html')


def register(request):
    """
    INPUT: a request
    USAGE: Instantiates and attaches appropriate attributes to user object
    OUTPUT: N/A
    """
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = Profile()

        user.username = username
        user.email = email

        user.set_password(password)

        # If attempt is made to register a Profile with a username that already exists,
        # reload the page with an error message.
        try:
            Profile.objects.get(username=username)
        except Profile.DoesNotExist:
            user.save()
        else:
            return render(request, 'register.html', {'username_error': ('Username %s exists.' % username)})

        usr = authenticate(username=username, password=password)

        if usr is not None:
            login(request, usr)
        return HttpResponseRedirect('/')

    return render(request, 'register.html', {})

def profile_page(request, mbr):
    """
    INPUT: a user object
    USAGE: to render out the profile page with the user as ontext
    OUTPUT: a rendered profile page
    """
    user = Profile.objects.get(username=mbr)
    context_dict = {'user': user}
    return render(request, 'profile_page.html', context_dict)

def log_in(request):
    """
    INPUT: a request
    USAGE: to log in the correct user if credentials are valid
    OUTPUT: a rendered profile page if successful else, login page
    """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/profile_page/' + str(user.username))
    return render(request, 'login.html', {})


def logout_view(request):
    """
    INPUT: a request
    USAGE: to logout the current user
    OUTPUT: a rendered home page
    """

    logout(request)
    return HttpResponseRedirect('/')


def check_if_username_exists(request):
    if request.method == 'POST':
        proposed_username = request.POST.get('proposed_username')

        try:
            Profile.objects.get(username = proposed_username)
        except Profile.DoesNotExist:
            response_data = {"username_exists":False,"username_exists_message":"Great, that username is available!"}
        else:
            response_data = {"username_exists":True,"username_exists_message":"Sorry, that username is already in use."}
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
       return HttpResponse(
            json.dumps({"error": "request.method was not POST"}),
            content_type="application/json"
        )