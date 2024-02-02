from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from bolgs.views import home
def about(request):

    return render(request, "about.html", {})




def logout_view(request):
    logout(request)
    return redirect(home)
    # Redirect to a success page.

def test_view(request):

    return render(request, "test.html", {})
    # Redirect to a success page.