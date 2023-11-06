import requests
from bs4 import BeautifulSoup, Tag
import sys
import random
import pokemonFactory

response = requests.get("https://pokemondb.net/pokedex/all")

pokemonSite = "https://pokemondb.net/pokedex/all"
soup = BeautifulSoup(response.text, 'lxml')
    
def checkIfSiteIsAvailable(site: str) -> bool:
    response = requests.get(site)
    if response.status_code != 200:
        return False
    return True

def getBeautifulSoupInstanceFromSite(site: str, parser: str) -> BeautifulSoup:
    response = requests.get(site)
    return BeautifulSoup(response.text, parser)

def getAllPokemonNames(bs: BeautifulSoup) -> list:
    pokemon: Tag
    pokemons = []
    for pokemon in soup.find("tbody").find_all("tr"):
        pokemons.append(pokemon.a.contents[0])
    return pokemons

def IsValidPokemon(pokemonList: list, pokemon: str) -> bool:
    pokemon = pokemon.capitalize()
    for el in pokemonList:
        if pokemon == el:
            return True
    return False

def getRandomPokemon(pokeList: list) -> str:
    return random.choice(pokeList)