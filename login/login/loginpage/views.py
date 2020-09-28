from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.
from .models import Products


def LoginPage(request):

    data = Products.objects.all()

    context = { 'data': data}

    return render(request,'loginpage/layout.html', context)

def profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts)
        return render(request, 'loginpage/user.html', {"query":query})
    else:
        return render(request, 'loginpage/layout.html', {})


def logout(request):
    try:
        del request.session['username']
    except:
     pass
    return redirect("profile")
