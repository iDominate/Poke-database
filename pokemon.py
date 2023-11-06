class BasicInfo(object):
    def __init__(self, type: list, species: str, height: str, weight: str, abilities: list) -> None:
        self.type = type
        self.species = species
        self.height = height
        self.weight = weight
        self.abilities = abilities
        
    def to_dict(self) -> dict:
        return {
            'Type': self.type,
            'Species': self.species,
            'Height': self.height.replace("\xa0", " "),
            'Weight': self.weight.replace("\xa0", " "),
            'Abilites': self.abilities
        }
class NumericInfo(object):
    def __init__(self, HP: str, attack: str, defense: str, sAttack: str, sDefense: str, speed: str) -> None:
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.sAttack = sAttack
        self.sDefense = sDefense
        self.speed = speed
    
    def to_dict(self) -> dict:
        return {
            'HP': self.HP,
            'Attack': self.attack,
            'Defense': self.defense,
            'sAttack': self.defense,
            'sDefense': self.sDefense,
            'Speed': self.speed
        }
    

class Pokemon(object):
    def __init__(self, basic: BasicInfo, numericInfo: NumericInfo, evolution: list, ety: dict ) -> None:
        self.basic = basic
        self.numericInfo = numericInfo
        self.evolution = evolution
        self.ety = ety
        
    def to_dict(self):
        return {
            'basic': self.basic.to_dict(),
            'numeric': self.numericInfo.to_dict(),
            'evolution': self.evolution,
            'etymology': self.ety
        }
        
    
    




        