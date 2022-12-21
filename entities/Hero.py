from Errors import InvalidHeroData,InvalidHeroClass
class Hero():
    HERO_TYPES=("Warrior","Mage","Priest","Rogue")
    GENDERS=("Male","Female")
    def __init__(self,name,gender,HeroClass)->None:
        if(type(name)!=str or len(name)<4 or gender not in Hero.GENDERS): raise InvalidHeroData()
        if(HeroClass not in Hero.HERO_TYPES): raise InvalidHeroClass()
        self.name=name
        self.gender=gender
        self.HeroClass=HeroClass
        self.weapon
        self.item
    def print(self):
        return f"Hero({self.name}, {self.HeroClass},  {self.weapon.print()}, {self.item.print()})"
    def add_weapon(self,weapon):
        self.weapon=weapon
    def add_item(self,item):
        self.item=item
