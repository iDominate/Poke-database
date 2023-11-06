from flask import Blueprint, jsonify
import pokemonFactory
from bs4 import BeautifulSoup
from response import PokemonResponse
import basic_poke_func
pokemonRoutes = Blueprint("pokemon", __name__, url_prefix='/pokemon/api/v1')

def get_pokemon_soup(pokemon: str) -> BeautifulSoup:
    soup = pokemonFactory.PokemonFactory.getSoup(pokemonFactory.baseUrl, pokemon)
    return soup

def get_database_soup() -> BeautifulSoup:
    soup = basic_poke_func.getBeautifulSoupInstanceFromSite(basic_poke_func.pokemonSite, 'lxml')
    return soup

@pokemonRoutes.get('/<pokemon>/attack')
def get_attack(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['attack'] = pokemonFactory.PokemonFactory.getNumericInfo(soup).attack
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Attack Fetched', data).to_dict())

def get_random_pokemon_name():
    soup = get_database_soup()
    pokeName = basic_poke_func.getRandomPokemon(basic_poke_func.getAllPokemonNames(soup))
    return pokeName

@pokemonRoutes.get('/random/name')
def get_random_name():
    pokeName = get_random_pokemon_name()
    return jsonify(PokemonResponse.getSuccessMessage('Got Random Pokemon Name', pokeName).to_dict())

@pokemonRoutes.get('/<pokemon>/defense')
def get_defense(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['defense'] = pokemonFactory.PokemonFactory.getNumericInfo(soup).defense
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Defense Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/HP')
def get_HP(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['HP'] = pokemonFactory.PokemonFactory.getNumericInfo(soup).HP
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon HP Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/sDefense')
def get_sDefense(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['sDefense'] = pokemonFactory.PokemonFactory.getNumericInfo(soup).sDefense
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Special Defense Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/sAttack')
def get_sAttack(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['sAttack'] = pokemonFactory.PokemonFactory.getNumericInfo(soup).sAttack
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Special Attack Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/speed')
def get_speed(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['speed'] = pokemonFactory.PokemonFactory.getNumericInfo(soup).speed
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/types')
def get_types(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['types'] = pokemonFactory.PokemonFactory.getBasicInfo(soup).type
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/species')
def get_species(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['species'] = pokemonFactory.PokemonFactory.getBasicInfo(soup).species
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/height')
def get_height(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['height'] = pokemonFactory.PokemonFactory.getBasicInfo(soup).height.replace("\xa0", " ")
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/weight')
def get_weight(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['weight'] = pokemonFactory.PokemonFactory.getBasicInfo(soup).weight.replace("\xa0", " ")
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/abilities')
def get_abilities(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['abilities'] = pokemonFactory.PokemonFactory.getBasicInfo(soup).abilities
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/evo')
def get_evolution(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['evolution'] = pokemonFactory.PokemonFactory.getEvoDetails(soup)
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/ety')
def get_etymology(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['etymology'] = pokemonFactory.PokemonFactory.getEtymology(soup)
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/basic')
def get_basic_info(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['basic'] = pokemonFactory.PokemonFactory.getBasicInfo(soup).to_dict()
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/numeric')
def get_numeric_info(pokemon: str):
    soup = get_pokemon_soup(pokemon)
    data = {}
    data['pokemon'] = pokemon
    data['numeric'] = pokemonFactory.PokemonFactory.getNumericInfo(soup).to_dict()
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon Speed Fetched', data).to_dict())

@pokemonRoutes.get('/<pokemon>/all')
def get_pokemon_all_data(pokemon: str):
    data = {}
    data['pokemon'] = pokemon
    data['all data'] = pokemonFactory.PokemonFactory.getPokemon(pokemonFactory.baseUrl, pokemon).to_dict()
    return jsonify(PokemonResponse.getSuccessMessage('Pokemon data Fetched', data).to_dict())
    


