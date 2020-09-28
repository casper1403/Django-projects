from django.shortcuts import render
from trainer.models import Pokemon, Profile
import random
global pk

pk = random.randint(1, 800)
# Create your views here.
def CatchView(request):
    global pk
    context = dict()

    if request.POST.get('Search') == "Find":
        pk = random.randint(1, 800)
        context['pokemon'] = Pokemon.objects.get(pokedex_number=pk)

    if request.POST.get('Catch') == "Try":
        context['pokemon'] = Pokemon.objects.get(pokedex_number=pk)
        change = context['pokemon']
        capture_change = random.randint(0, 300)
        if change.capture_rate > capture_change:
            request.user.Profile.pokemon.add(Pokemon.objects.get(pokedex_number=pk))
            context['caught'] = "Caught"
            pk = random.randint(1, 800)
            context['pokemon'] = Pokemon.objects.get(pokedex_number=pk)
        else:
            pk = random.randint(1, 800)
            context['pokemon'] = Pokemon.objects.get(pokedex_number=pk)


    return render(request, 'catch.html',context)
