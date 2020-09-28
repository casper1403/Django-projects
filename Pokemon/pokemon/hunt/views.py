from django.shortcuts import render
from django.contrib.auth.models import User
from trainer.models import Pokemon
from .models import Hunters
from django.contrib import messages

def HuntView(request):

    context = dict()
    current_user = User.objects.get(username=request.user)
    context['pokemon'] = request.user.Profile.pokemon.all()

    if request.POST:

        if 'poke' in request.POST:
            PokemonIstance = Pokemon.objects.get(pokedex_number=request.POST.get('poke'))
            if len(request.user.Hunters.pokemon.all()) < 6:
                request.user.Hunters.pokemon.add(PokemonIstance)
            if len(request.user.Hunters.pokemon.all()) == 6:
                messages.warning(request, 'You can only bring 6 pokemon')

        if 'delete' in request.POST:
            request.user.Hunters.pokemon.remove(Pokemon.objects.get(pokedex_number=request.POST['delete']))

    if len(request.user.Hunters.pokemon.all()) > 0:
        context['battle'] = True

    context['hunters'] = request.user.Hunters.pokemon.all()


    return render(request,'battle.html', context)


def FightView(request):

    return render(request, 'fight.html')
