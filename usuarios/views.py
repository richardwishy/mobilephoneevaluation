from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.


def logout_view(request):
    logout(request)
    # Redirect to a success page.
