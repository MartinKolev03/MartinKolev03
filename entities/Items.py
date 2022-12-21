from Errors import InvalidItemData,InvalidWeaponData
class Item():
    def __init__(self,name):
        if(type(name)!=str or not name.isAlpha()): raise InvalidItemData()
        self.name=name
        self.durability=100
    def print(self):
        return f"Item({self.name}, {self.durability})"
class Weapon(Item):
    def __init__(self,name,attack):
        super.__init__(self,name)
        if(type(attack)!=int or attack<=0): raise InvalidWeaponData()
        self.attack=attack
    def print(self):
        return f"Weapon({self.name}, {self.durability}, {self.attack})"