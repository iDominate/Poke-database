import pokemon
from bs4 import BeautifulSoup
import requests
import basic_poke_func


baseUrl = "https://pokemondb.net/pokedex/"
dbUrl = "https://pokemondb.net/pokedex/all"

class PokemonFactory(object):
    
    soup: BeautifulSoup
    
    @staticmethod
    def getTypes(table) -> list:
        #print(table.find_all('a', {'class': 'type-icon'})[0].text)
        types = []
        for element in table.find_all('a', {'class': 'type-icon'}):
            types.append(element.text)
        return types
    @staticmethod
    def getSpecies(table) -> str:
        return table.find_all('tr')[2].td.text
        
    @staticmethod       
    def getHeight(table) -> str:
        height = table.find_all("tr")[3]
        return height.td.text
    
    @staticmethod
    def getWeight(table) -> str:
        weight = table.find_all("tr")[4]
        return weight.td.text
    
    @staticmethod
    def getAbilities(table) -> list:
        abilitiesList = []
        abilities = table.find_all("tr")[5]
        ab = abilities.find_all('a')
        for i in ab:
            abilitiesList.append(i.text)
        return abilitiesList
    
    @staticmethod
    def getHP(table) -> str:
        HP = table.find_all('tr')[0]
        return HP.td.text
        
    def getAttack(table) -> str:
        attack = table.find_all('tr')[1]
        return attack.td.text
    
    @staticmethod
    def getDefense(table) -> str:
        defense = table.find_all('tr')[2]
        return defense.td.text
    
    @staticmethod
    def getSAttack(table) -> str:
        sAttack = table.find_all('tr')[3]
        return sAttack.td.text
        
    @staticmethod
    def getSAttack(table) -> str:
        sAttack = table.find_all('tr')[3]
        return sAttack.td.text
    
    @staticmethod
    def getSDefense(table) -> str:
        sDefense = table.find_all('tr')[4]
        return sDefense.td.text
    
    @staticmethod
    def getSpeed(table) -> str:
        speed = table.find_all('tr')[5]
        return speed.td.text
    
    @staticmethod
    def getEvo0(table) -> str:
        try:
            evo0 = table.find_all("div", class_="infocard")[0]
            return evo0.find_all("span")[1].text.split(' ')[1]
        except:
            return ""
            
    @staticmethod   
    def getEvo1(table) -> str:
        evo0 = table.find_all("div", class_="infocard")[1]
        if evo0 == None:
            return ""
        else:
            return evo0.find_all("span")[1].text.split(' ')[1]
    
    @staticmethod
    def getEvo2(table) -> str:
        try:
            evo0 = table.find_all("div", class_="infocard")[2]
            return evo0.find_all("span")[1].text.split(' ')[1]
        except Exception as e:
            return ""
            
    @staticmethod
    def getEtymology(table) -> str:
        ety = table.find("dl", {"class": "etymology"})
        final = {name.text: meaning.text for name in ety.find_all("dt") for meaning in ety.find_all("dd")}
        return final
    
    @staticmethod
    def getSoup(baseUrl: str, pokemonName: str) -> BeautifulSoup:
        fullUrl =f'{baseUrl}{pokemonName}'
        response = requests.get(fullUrl)
        
        soup = BeautifulSoup(response.text, 'lxml')
        PokemonFactory.soup = soup
        return PokemonFactory.soup
        
    @staticmethod
    def getBasicInfo(soup: BeautifulSoup) -> pokemon.BasicInfo:
        vitalsTable0 = soup.find_all('table', class_='vitals-table')[0]
        #print(vitalsTable0)
        type = PokemonFactory.getTypes(vitalsTable0)
        species = PokemonFactory.getSpecies(vitalsTable0)
        height = PokemonFactory.getHeight(vitalsTable0)
        weight = PokemonFactory.getWeight(vitalsTable0)
        abilities = PokemonFactory.getAbilities(vitalsTable0)
        
        return pokemon.BasicInfo(type, species, height, weight, abilities)
    
    @staticmethod
    def getNumericInfo(soup: BeautifulSoup) -> pokemon.NumericInfo:
        vitalsTable2 = soup.find_all('table', {'class': 'vitals-table'})[3]
        hp = PokemonFactory.getHP(vitalsTable2)
        attack = PokemonFactory.getAttack(vitalsTable2)
        defense = PokemonFactory.getDefense(vitalsTable2)
        sAttack = PokemonFactory.getSAttack(vitalsTable2)
        sDefense = PokemonFactory.getSDefense(vitalsTable2)
        speed = PokemonFactory.getSpeed(vitalsTable2)
        return pokemon.NumericInfo(hp, attack, defense, sAttack, sDefense, speed)
    
    @staticmethod
    def getEvoDetails(soup: BeautifulSoup) -> dict:
        evoDict = {}
        evoTable = soup.find("div", class_="infocard-list-evo")
        if evoTable == None:
            return evoDict
        
        evoDict['Basic'] = PokemonFactory.getEvo0(soup)
        
        evoDict['First'] = PokemonFactory.getEvo1(soup)
        evo2 = PokemonFactory.getEvo2(soup)
        if evo2 == None:   
            pass
        else:
            evoDict['Second'] = PokemonFactory.getEvo2(soup)
        return evoDict
    
    @staticmethod
    def getEtymology(soup: BeautifulSoup) -> dict:
        ety = soup.find("dl", {"class": "etymology"})
        final = {name.text: meaning.text for name in ety.find_all("dt") for meaning in ety.find_all("dd")}
        return final
    
    @staticmethod
    def getPokemon(baseUrl: str, pokemonName: str) -> pokemon.Pokemon:
        soup = PokemonFactory.getSoup(baseUrl, pokemonName)
        basicInfo = PokemonFactory.getBasicInfo(soup)
        numericInfo = PokemonFactory.getNumericInfo(soup)
        evoInfo = PokemonFactory.getEvoDetails(soup)
        etymology = PokemonFactory.getEtymology(soup)
        return pokemon.Pokemon(basicInfo, numericInfo, evoInfo, etymology)
        
if __name__ == "__main__":
    baseUrl = "https://pokemondb.net/pokedex/"
    dbUrl = "https://pokemondb.net/pokedex/all"
    zeraora = PokemonFactory.getPokemon(baseUrl, basic_poke_func.getRandomPokemon(basic_poke_func.getAllPokemonNames(basic_poke_func.getBeautifulSoupInstanceFromSite(dbUrl, 'lxml'))))
    print(zeraora.ety)
    

    

