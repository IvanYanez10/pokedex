from logging import PlaceHolder
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import requests

class PokeChosen(forms.Form):
    varPokeChosen = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search'})) #Poke name or ID

def index(request):
    flag = False
    url = "https://pokeapi.co/api/v2/pokemon/1"
    
    if request.method == "POST":
        inputUser = PokeChosen(request.POST)        
        if inputUser.is_valid():
            inputUserClened = inputUser.cleaned_data["varPokeChosen"].lower()
            url = "https://pokeapi.co/api/v2/pokemon/"+inputUserClened
    
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        flag = True
        response = requests.get("https://pokeapi.co/api/v2/pokemon/1")        
    
    dataJson = response.json()
    namePokemon = dataJson["forms"][0]["name"].capitalize()
    idPokemon = dataJson["id"]    
    heightPokemon = float(dataJson["height"]) / 10  
    weightPokemon = float(dataJson["weight"]) / 10
    imageUrlPokemon = dataJson["sprites"]["other"]["home"]["front_default"]
    typesPokemon = []
    statsPokemon = []

    for i in dataJson["types"]:
        typesPokemon.append({ "name":i["type"]["name"]})
    
    for i in dataJson["stats"]:
        statsPokemon.append([i["stat"]["name"], i["base_stat"]])
    

    return render(request, 'pokedexApp/index.html', {
        "flag": flag,
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
