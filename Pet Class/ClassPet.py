# Add designs in the program 
from termcolor import colored
from pyfiglet import Figlet

f = Figlet(font = "isometric3", width = 240)
print(colored(f.renderText(" Pet Class"), "light_green"))
print(colored("=" * 135, "light_green"))

# Create a class named Pet
class Pet:
    # Create constructor that creates a Pet with the specified name, animal type, and age
    def __init__(self, name, animal_type, age):
        # Create instance variable 
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Create accessor (getter) method for name
    def get_name(self):
        return self.__name
    
    # Create mutator (setter) method for name
    def set_name(self, name):
        self.__name = name

    # Create accessor (getter) method for animal type
    def get_animal_type(self):
        return self.__animal_type
    
    # Create mutator (setter) method for animal type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Create accessor (getter) method for age
    def get_age(self):
        return self.__age

    # Create mutator (setter) method for age
    def set_age(self, age):
        self.__age = age