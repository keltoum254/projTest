from django.shortcuts import render
from django.contrib.auth import logout

def about(request):

    return render(request, "about.html", {})




def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html", {})
    # Redirect to a success page.