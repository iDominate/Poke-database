from unittest import TestCase, main
from main import app
from json import loads
from response import PokemonResponse

class TestMain(TestCase):
    
    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client()
    
    def test_get_random_pokemon_name(self):
        response = self.app.get("/pokemon/api/v1/random/name")
        response_json = loads(response.text)
        # print(response_json)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response_json['data'], str)
        self.assertEqual(response_json['status'], 'ok')

    def test_get_attack(self):
        response = self.app.get("/pokemon/api/v1/gengar/attack")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(int(response_json['data']['attack']), int)
        self.assertIsInstance(response_json['data']['pokemon'], str)

    def test_get_defense(self):
        response = self.app.get("/pokemon/api/v1/gengar/defense")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(int(response_json['data']['defense']), int)
        self.assertIsInstance(response_json['data']['pokemon'], str)

    def test_get_HP(self):
        response = self.app.get("/pokemon/api/v1/gengar/HP")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(int(response_json['data']['HP']), int)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_sDefense(self):
        response = self.app.get("/pokemon/api/v1/gengar/sDefense")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(int(response_json['data']['sDefense']), int)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_sAttack(self):
        response = self.app.get("/pokemon/api/v1/gengar/sAttack")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(int(response_json['data']['sAttack']), int)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_speed(self):
        response = self.app.get("/pokemon/api/v1/gengar/speed")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(int(response_json['data']['speed']), int)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_types(self):
        response = self.app.get("/pokemon/api/v1/gengar/types")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        # print(response_json)
        self.assertIsInstance(response_json['data']['types'], list)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_species(self):
        response = self.app.get("/pokemon/api/v1/gengar/species")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        # print(response_json)
        self.assertIsInstance(response_json['data']['species'], str)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_height(self):
        response = self.app.get("/pokemon/api/v1/gengar/height")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        # print(response_json)
        self.assertIsInstance(response_json['data']['height'], str)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_weight(self):
        response = self.app.get("/pokemon/api/v1/gengar/weight")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        # print(response_json)
        self.assertIsInstance(response_json['data']['weight'], str)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_abilities(self):
        response = self.app.get("/pokemon/api/v1/gengar/abilities")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        # print(response_json)
        self.assertIsInstance(response_json['data']['abilities'], list)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_evo_details(self):
        response = self.app.get("/pokemon/api/v1/gengar/evo")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response_json['data']['evolution'], dict)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_etymology(self):
        response = self.app.get("/pokemon/api/v1/gengar/ety")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response_json['data']['etymology'], dict)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_basic(self):
        response = self.app.get("/pokemon/api/v1/gengar/basic")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        # print(response_json)
        self.assertIsInstance(response_json['data']['basic'], dict)
        self.assertIsInstance(response_json['data']['pokemon'], str)

    def test_get_numeric(self):
        response = self.app.get("/pokemon/api/v1/gengar/numeric")
        response_json: dict = loads(response.text)
        self.assertEqual(response.status_code, 200)
        # print(response_json)
        self.assertIsInstance(response_json['data']['numeric'], dict)
        self.assertIsInstance(response_json['data']['pokemon'], str)
        
    def test_get_pokemon(self):
        response = self.app.get('/pokemon/api/v1/gengar/all')
        pokemon = loads(response.text)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(pokemon['data'], dict)
        self.assertIsInstance(pokemon['data']['all data']['basic'], dict)
        self.assertIsInstance(pokemon['data']['all data']['numeric'], dict)
        self.assertIsInstance(pokemon['data']['all data']['evolution'], dict)
        self.assertIsInstance(pokemon['data']['all data']['etymology'], dict)
        
    
if __name__ == "__main__":
    main()
        