from unittest import TestCase, main
from pokemonFactory import baseUrl, dbUrl
from unittest.mock import patch
from bs4 import BeautifulSoup
import basic_poke_func

class TestBasicPokeFunc(TestCase):
    def setUp(self) -> None:
        self.baseUrl = baseUrl
        self.dbUrl = dbUrl
        self.pokemon = 'gengar' 
        
        
    def test_check_if_site_is_availabl_false(self):
        with patch("basic_poke_func.requests.get") as mocked_get:
            mocked_get.return_value.status_code = 404
            self.assertFalse(basic_poke_func.checkIfSiteIsAvailable(self.dbUrl))
            
    def test_check_if_site_is_availabl_true(self):
            with patch("basic_poke_func.requests.get") as mocked_get:
                mocked_get.return_value.status_code = 200
                self.assertTrue(basic_poke_func.checkIfSiteIsAvailable(self.dbUrl))
                
    def test_get_beautiful_soup_instance(self):
        with patch("basic_poke_func.requests.get") as mocked_get:
            mocked_get.return_value.text = "Hello World"
            self.assertIsInstance(basic_poke_func.getBeautifulSoupInstanceFromSite("Hello", 'lxml'), BeautifulSoup)
            
    def test_get_all_pokemon_names(self):
        site = basic_poke_func.getBeautifulSoupInstanceFromSite(self.dbUrl, 'lxml')
        pokeList: list = basic_poke_func.getAllPokemonNames(site)
        self.assertIsInstance(pokeList, list)
    
    def test_is_valid_pokemon_returns_false(self):
        site = basic_poke_func.getBeautifulSoupInstanceFromSite(self.dbUrl, 'lxml')
        pokeList: list = basic_poke_func.getAllPokemonNames(site)
        result = basic_poke_func.IsValidPokemon(pokeList, "Hello")
        self.assertFalse(result)
        
    def test_is_valid_pokemon_returns_true(self):
        site = basic_poke_func.getBeautifulSoupInstanceFromSite(self.dbUrl, 'lxml')
        pokeList: list = basic_poke_func.getAllPokemonNames(site)
        result = basic_poke_func.IsValidPokemon(pokeList, "gengar")
        self.assertTrue(result)
    
    def test_get_random_pokemon(self):
        site = basic_poke_func.getBeautifulSoupInstanceFromSite(self.dbUrl, 'lxml')
        pokeList: list = basic_poke_func.getAllPokemonNames(site)
        result = basic_poke_func.getRandomPokemon(pokeList)
        self.assertIsNotNone(result)
    
    
    

if __name__ == '__main__':
    main()