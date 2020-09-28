from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from trainer.models import Pokemon
from api.serializers import PokemonSerializer


@csrf_exempt
def pokemon_list(request, health, att):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        pokemon = Pokemon.objects.filter(hp__gt=health,attack__gt=att)

        serializer = PokemonSerializer(pokemon, many=True)
        return JsonResponse(serializer.data, safe=False)


def generation_list(request, generation):

    if request.method == 'GET':
        pokemon = Pokemon.objects.filter(generation__exact=generation)
        serializer = PokemonSerializer(pokemon, many=True)
        return JsonResponse(serializer.data, safe=False)
