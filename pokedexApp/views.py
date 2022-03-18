from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import requests

class PokeChosen(forms.Form):
    varPokeChosen = forms.CharField(label= "Chose: ")

def index(request):

    url = "https://pokeapi.co/api/v2/pokemon/1"

    if request.method == "POST":
        inputUser = PokeChosen(request.POST)
        if inputUser.is_valid():
            inputUserClened = inputUser.cleaned_data["varPokeChosen"].lower()
            url = "https://pokeapi.co/api/v2/pokemon/"+inputUserClened
    
    response = requests.get(url)
    dataJson = response.json()
    namePokemon = dataJson["forms"][0]["name"].capitalize()
    idPokemon = dataJson["id"]    
    heightPokemon = float(dataJson["height"]) / 10  
    weightPokemon = float(dataJson["weight"]) / 10
    imageUrlPokemon = dataJson["sprites"]["other"]["home"]["front_default"]
    typesPokemon = []
    statsPokemon = []

    for i in dataJson["types"]:
        typesPokemon.append(i["type"]["name"])
    
    for i in dataJson["stats"]:
        statsPokemon.append([i["stat"]["name"], i["base_stat"]])
       

    return render(request, 'pokedexApp/index.html', {
        "dataJson": dataJson,
        "namePokemon": namePokemon,
        "idPokemon": idPokemon,
        "typesPokemon": typesPokemon,
        "statsPokemon": statsPokemon,
        "heightPokemon": heightPokemon,
        "weightPokemon": weightPokemon,
        "imageUrlPokemon": imageUrlPokemon,
        "pkc": PokeChosen()
        })