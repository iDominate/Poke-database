from unittest import TestCase, main
import pokemonFactory
from bs4 import BeautifulSoup
import pokemon
class TestPokemonFactory(TestCase):
    
    def setUp(self) -> None:
        self.baseUrl = pokemonFactory.baseUrl
        self.dbUrl = pokemonFactory.dbUrl
        self.pokemonName = 'gengar'
    
    def test_get_soup(self):
        soup = pokemonFactory.PokemonFactory.getSoup(self.baseUrl, self.pokemonName)
        self.assertIsInstance(soup, BeautifulSoup)
    
    def test_get_basic_info(self):
        soup = pokemonFactory.PokemonFactory.getSoup(self.baseUrl, self.pokemonName)
        basic = pokemonFactory.PokemonFactory.getBasicInfo(soup)
        self.assertIsInstance(basic, pokemon.BasicInfo)
        self.assertIsNotNone(basic)
    
    def test_numeric_info(self):
        soup = pokemonFactory.PokemonFactory.getSoup(self.baseUrl, self.pokemonName)
        numeric = pokemonFactory.PokemonFactory.getNumericInfo(soup)
        self.assertIsInstance(numeric, pokemon.NumericInfo)
        self.assertIsNotNone(numeric)
        
    def test_get_evo_details(self):
        soup = pokemonFactory.PokemonFactory.getSoup(self.baseUrl, self.pokemonName)
        evoDetails = pokemonFactory.PokemonFactory.getEvoDetails(soup)
        self.assertIsInstance(evoDetails, dict)
        self.assertEqual(len(evoDetails), 3)
        
    def test_get_etymology(self):
        soup = pokemonFactory.PokemonFactory.getSoup(self.baseUrl, self.pokemonName)
        etDetails = pokemonFactory.PokemonFactory.getEtymology(soup)
        self.assertIsInstance(etDetails, dict)
        self.assertEqual(len(etDetails), 1)
        
        
        
        




if __name__ == "__main__":
    main()