class InvalidHeroData(Exception):
    def __init__(self, message="Invalid Hero data was entered", *args: object) -> None:
        super().__init__(message, *args)
class InvalidWeaponData(Exception):
    def __init__(self, message="Invalid Weapon", *args: object) -> None:
        super().__init__(message, *args)
class InvalidItemData(Exception):
    def __init__(self, message="Invalid Item", *args: object) -> None:
        super().__init__(message, *args)
class HeroNotFound(Exception):
    def __init__(self, message="Hero not found", *args: object) -> None:
        super().__init__(message, *args)
class HeroAlreadyExsists(Exception):
    def __init__(self, message="Hero already exists", *args: object) -> None:
        super().__init__(message, *args)
class InvalidHeroClass(Exception):
    def __init__(self, message="Invalid HeroClass was entered", *args: object) -> None:
        super().__init__(message, *args)
class InvalidCommand(Exception):
    def __init__(self, message="Invalid command was chosen", *args: object) -> None:
        super().__init__(message, *args)