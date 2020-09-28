import requests


pokemon = requests.get('http://127.0.0.1:8000/api/')

print(pokemon.content)
