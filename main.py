from entities import Hero
from Errors import InvalidCommand,HeroNotFound,HeroAlreadyExsists


class Menu:
    def print_menu(self):
        print("1. Create a new character")

    def command_create_character(self, name, sex, ch_class):
        pass

    def run(self):
        while True:
            choice = input("Choose an item from the menu: \n> ")
            try:
                if choice == "1":
                    name = input("Enter the character name (alpha-numeric): ")
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '__main__':
    menu = Menu()
    menu.run()