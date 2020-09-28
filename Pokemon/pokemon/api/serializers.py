from rest_framework import serializers
from trainer.models import Pokemon

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['legendary',
        'name',
        'pokedex_number',
        'attack',
        'defense',
        'hp',
        'base_happiness',
        'sp_attack',
        'sp_defense',
        'speed',
        'generation',
        "is_legendary",
        "capture_rate",]
