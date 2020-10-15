from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import BookModel, GameModel
from dal import autocomplete
import numpy as np

FIELDNAMES = ['romance',
'scifi',
'adventure',
'action',
'drama',
'fantasy',
'mystery',
'supernatural',
'horror',
'historical',
'realistic',
'crime',
'comedy',
'war',
'manga_anime',
'sport']

def ReturnGames(game):
    # From the game fetch all the fields that have a 1 and put them in list
    PositiveFields = list()
    for field in FIELDNAMES:
        field_object = GameModel._meta.get_field(field)
        field_value = field_object.value_from_object(game)
        if field_value == 1:
            PositiveFields.append(field)

    # query the database for book based on the fields that the game has. FieldSet is a list of sets
    FieldSet = list()
    for field in PositiveFields:
        bookObjects = BookModel.objects.raw(f'SELECT * FROM website_bookmodel WHERE {field} == 1;')
        Tempset = list()
        for i in bookObjects:
            Tempset.append(i)
        FieldSet.append(set(Tempset))

    # If onnly one fieldset get the fields with the highest rating. Randomly select 5. Sort them and return
    # if tag is one
    if len(FieldSet) <= 1:
        sorted = list(FieldSet[0])
        sorted.sort(key=lambda x: x.average_rating, reverse=True)
        highestList = sorted[:]

        if len(highestList) >= 100:
            highestList = sorted[0:100]
            randomFive = [highestList[i] for i in np.random.choice(range(100), 5, replace=False)]
            randomFive.sort(key=lambda x: x.average_rating, reverse=True)
            ReturnFive = randomFive[:]
            return ReturnFive

        if len(highestList) < 100 and len(highestList) >= 5:
            randomFive = [highestList[i] for i in np.random.choice(range(len(highestList)), 5, replace=False)]
            randomFive.sort(key=lambda x: x.average_rating, reverse=True)
            ReturnFive = randomFive[:]
            return ReturnFive

        if len(highestList) < 5:
            return list(FieldSet[0])[0:5]

    else:
        sorted = list(set.intersection(*FieldSet))
        sorted.sort(key=lambda x: x.average_rating, reverse=True)
        highestList = sorted[:]

        if len(highestList) >= 100:
            highestList = sorted[0:100]
            randomFive = [highestList[i] for i in np.random.choice(range(100), 5, replace=False)]
            randomFive.sort(key=lambda x: x.average_rating, reverse=True)
            ReturnFive = randomFive[:]
            return ReturnFive

        if len(highestList) < 100 and len(highestList) >= 5:
            randomFive = [highestList[i] for i in np.random.choice(range(len(highestList)), 5, replace=False)]
            randomFive.sort(key=lambda x: x.average_rating, reverse=True)
            ReturnFive = randomFive[:]
            return ReturnFive

        if len(highestList) < 5:
            return list(FieldSet[0])[0:5]

def homeView(request):
    context = dict()
    if 'term' in request.GET:
        qs = GameModel.objects.all()
        qs = qs.filter(name__istartswith=request.GET.get('term'))
        title = [str(i) for i in qs]
        viewed = title[0:5]
        return JsonResponse(viewed, safe=False)

    if 'game' in request.GET:
        game = request.GET.get('game')
        if len(GameModel.objects.filter(name=game)) == 1:
            context['available'] = False
            return redirect('show',game=game)
        else:
            context['available'] = "This entity was not found in the database"
        return render(request, 'home.html',context)
    return render(request, 'home.html',context)

def showView(request, game):
    context = dict()
    context['books'] = ReturnGames(GameModel.objects.filter(name=game)[0])

    return render(request, 'show.html',context)

def bookView(request, pk):
    context = dict()
    context['book'] = BookModel.objects.get(id=pk)
    context['year'] = str(BookModel.objects.get(id=pk).original_publication_year)[0:-1]
    return render(request, 'book.html', context)

def aboutView(request):
    return render(request, 'about.html')
