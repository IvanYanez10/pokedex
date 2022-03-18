from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class pokechosencl(forms.Form):
    pokechosen = forms.CharField(label = "Ingresa un Pokemon")

ditto = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/132.png"

def index(request):
    pkimg = "none"
    if request.method == 'POST':
        pkFormUser = pokechosencl(request.POST)
        if pkFormUser.is_valid():
            pkFormUserCleaned = pkFormUser.cleaned_data['pokechosen']
            pkFormUserCleaned.lower()
            if pkFormUserCleaned == 'ditto':
                pkimg = ditto

        else:
            return render(request, 'pokedexApp/index.html', {"pkc": pokechosencl(), "pkimg": pkimg}) 
    return render(request, 'pokedexApp/index.html', {"pkc": pokechosencl(), "pkimg": pkimg})
