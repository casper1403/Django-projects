from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def HeroViewSet(request, name):

    hero = Hero.objects.filter(name__contains=name)
    serializer = HeroSerializer(hero, many=True)
    return JsonResponse(serializer.data,safe=False)
