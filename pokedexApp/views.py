from django.shortcuts import render
from django.http import HttpResponse
import requests
import logging

def index(request):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/bulbasaur')
    dataJson = response.json()
    namePokemon = dataJson["forms"][0]["name"].capitalize()
    idPokemon = dataJson["id"]    
    heightPokemon = float(dataJson["height"]) / 10  
    weightPokemon = float(dataJson["weight"]) / 10
    imageUrlPokemon = dataJson["sprites"]["other"]["home"]["front_default"]
    typesPokemon = []
    statsPokemon = []

    # checar si nada mas tiene un tipo
    for i in dataJson["types"]:
        #logging.debug("Log message goes here.")
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
        "imageUrlPokemon": imageUrlPokemon
        })
