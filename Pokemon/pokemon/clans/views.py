from django.shortcuts import render
from django.contrib.auth.models import Group


# Create your views here.
def ClansView(request):

    if request.POST:
        print(request.POST['group'])


    return render(request, 'clans.html')
