import pandas as pd

import json
df = pd.read_csv('pokemon.csv')




df2 = df[['name', 'pokedex_number','attack','defense', 'hp','base_happiness','sp_attack', 'sp_defense', 'speed', 'generation', 'is_legendary','capture_rate']]
df2.insert(0, 'model', 'trainer.Pokemon')
df2.insert(1, 'pk', df['pokedex_number'])

df3 = df2[['model','pk']]

placeholder = []



df2.at[773, 'capture_rate'] = 30

for index, row in df2.iterrows():
    dict = {'model':'trainer.Pokemon',
    'pk':row['pk'],
    'fields':{'name':row['name'],
    'pokedex_number':row['pokedex_number'],
    'attack':row['attack'],
    'defense':row['defense'],
    'hp':row['hp'],
    'base_happiness':row['base_happiness'],
    'sp_attack':row['sp_attack'],
    'sp_defense':row['sp_defense'],
    'speed':row['speed'],
    'generation':row['generation'],
    'is_legendary':row['is_legendary'],
    'capture_rate':int(row['capture_rate']),
    }}
    placeholder.append(dict)


with open('PokemonStat.json', 'w') as fout:
    json.dump(placeholder , fout)
