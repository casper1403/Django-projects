from django.shortcuts import render, redirect
from .models import Pokemon, Profile
from .forms import TrainerForm
from django.contrib.auth.models import User

def TrainerView(request):

    context = dict()

    if request.user.is_authenticated:
        current_user = User.objects.get(username=request.user)
        context['pokemon'] = request.user.Profile.pokemon.all()

        # Fetch the form from forms.py
        form = TrainerForm(data=request.POST, instance=request.user)
        if request.method == 'POST':
            #instance is the Profile moder form the user
            form = TrainerForm(data=request.POST, instance=request.user.Profile)
            if form.is_valid():
                form.save()
                return redirect('trainer')
        else:
            form = TrainerForm()

        context['form'] = form


    return render(request, 'trainer.html',context)

#
def PokemonDeleteView(request, index=None):

    # pokemon = request.GET()
    request.user.Profile.pokemon.remove(Pokemon.objects.get(pokedex_number=index))

    return redirect('trainer')
