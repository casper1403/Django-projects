
import requests
layer = 'clouds_new'
z  = 1
x = 2
y =3
tempObject = requests.get(f"https://maps.owm.io/map/{layer}/{z}/{x}/{y}.png?&appid=5a0bffb1cd038523e6b4a23076521bab")
