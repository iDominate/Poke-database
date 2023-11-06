import main
import requests
from bs4 import BeautifulSoup

baseUrl = "https://pokemondb.net/pokedex/"

pokemon = "Mimikyu"

fullUrl =f'{baseUrl}{pokemon}'

response = requests.get(fullUrl)

soup = BeautifulSoup(response.text, 'lxml')
vitalsTable0 = soup.find_all('table', {'class': 'vitals-table'})[0]
print(vitalsTable0)

# def getTypes(table) -> list:
#     types = []
#     for element in table.find_all('a', {'class': 'type-icon'}):
#         types.append(element.text)
        
# def getSpecies(table) -> list:
#    for element in table.find_all('a', {'class': 'type-icon'}):
#         print(element.text)

# def getHeight(table) -> str:
#     height = table.find_all("tr")[3]
#     print(height.td.text)

# def getWeight(table) -> str:
#     weight = table.find_all("tr")[4]
#     print(weight.td.text)
    
# def getAbilities(table) -> list:
#     abilitiesList = []
#     abilities = table.find_all("tr")[5]
#     ab = abilities.find_all('a')
#     for i in ab:
#         abilitiesList.append(i.text)
        
# def getHP(table) -> str:
#     HP = table.find_all('tr')[0]
#     print(HP.td.text)

# def getAttack(table) -> str:
#     attack = table.find_all('tr')[1]
#     print(attack.td.text)

# def getDefense(table) -> str:
#     defense = table.find_all('tr')[2]
#     print(defense.td.text)
    
# def getSAttack(table) -> str:
#     sAttack = table.find_all('tr')[3]
#     print(sAttack.td.text)

# def getSDefense(table) -> str:
#     sDefense = table.find_all('tr')[4]
#     print(sDefense.td.text)

# def getSpeed(table) -> str:
#     speed = table.find_all('tr')[5]
#     print(speed.td.text)
    
# def getEvo0(table) -> str:
#     evo0 = table.find_all("div", class_="infocard")[0]
#     if evo0 == None:
#         return ""
#     else:
#         evo0.find_all("span")[1].text.split(' ')[1]

# def getEvo1(table) -> str:
#     evo0 = table.find_all("div", class_="infocard")[1]
#     if evo0 == None:
#         return ""
#     else:
#         evo0.find_all("span")[1].text.split(' ')[1]

# def getEvo2(table) -> str:
#     evo0 = table.find_all("div", class_="infocard")[2]
#     if evo0 == None:
#         return ""
#     else:
#         evo0.find_all("span")[1].text.split(' ')[1]

# def getEtymology(table) -> str:
#     ety = soup.find("dl", {"class": "etymology"})
#     final = {name.text: meaning.text for name in ety.find_all("dt") for meaning in ety.find_all("dd")}
#     return final
        
# Type
# for element in vitalsTable.find_all('a', {'class': 'type-icon'}):
#     print(element.text)

# Species
# species = vitalsTable.find_all("tr")[2]
# print(species.td.text)

#Height
# height = vitalsTable.find_all("tr")[3]
# print(height.td.text)

#Weight
# height = vitalsTable.find_all("tr")[4]
# print(height.td.text)

# Abilities
# abilities = vitalsTable.find_all("tr")[5]
# ab = abilities.find_all('a')
# for i in ab:
#     print(i.text)

vitalsTable2 = soup.find_all('table', {'class': 'vitals-table'})[3]

# HP
# HP = vitalsTable2.find_all('tr')[0]
# print(HP.td.text)

# Attack
# attack = vitalsTable2.find_all("tr")[1]
# print(attack.td.text)

# Defense
# defense = vitalsTable2.find_all("tr")[2]
# print(defense.td.text)

#Sp.attack
# a_attack = vitalsTable2.find_all("tr")[3]
# print(a_attack.td.text)

#Sp.defense
# sDefense = vitalsTable2.find_all("tr")[4]
# print(sDefense.td.text)

# Speed
# speed = vitalsTable2.find_all("tr")[5]
# print(speed.td.text)

# total = vitalsTable2.find_all("tr")[6]
# print(total.td.text)

# evoTable = soup.find("div", class_="infocard-list-evo")
# if evoTable == None:
#     print("does not evolve")
    
#evo0
# evo0 = evoTable.find_all("div", class_="infocard")[0]
# print(evo0.find_all("span")[1].text.split(' ')[1])

#evo1
# evo1 = evoTable.find_all("div", class_="infocard")[1]
# print(evo1.find_all("span")[1].text.split(' ')[1])

#evo2
# evo2 = evoTable.find_all("div", class_="infocard")[2]
# if evo2 == None:   
#     pass
# else:
#     print(evo0.find_all("span")[1].text.split(' ')[1])
    
# etmology
# ety = soup.find("dl", {"class": "etymology"})
# final = {name.text: meaning.text for name in ety.find_all("dt") for meaning in ety.find_all("dd")}
# print(final)
