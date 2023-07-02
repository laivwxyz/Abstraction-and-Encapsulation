# Add design in the program 
from termcolor import colored
from pyfiglet import Figlet

f = Figlet(font = 'isometric3', width = 240)
print(colored(f.renderText(' The Fan Class'), 'light_red'))
print(colored('=' * 185, 'light_red'))

# Create a class named Fan 
class Fan:
    # Create constant to denote the fan speed 
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Create constructor that creates a fan with the specified speed, radius, color and on
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False):
        # Create instance variable 
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # Create accessor (getter) method for speed 
    def get_speed(self):
        return self.__speed    
    
    # Create mutator (setter) method for speed
    def set_speed(self, speed):
        self.__speed = speed

    # Create accessor (getter) method for on
    def get_on(self):
        return self.__on
    
    # Create mutator (setter) method for on
    def set_on(self, on):
        self.__on = on

    # Create accessor (getter) method for radius
    def get_radius(self):
        return self.__radius
    
    # Create mutator (setter) method for radius
    def set_radius(self, radius):
        self.__radius = radius

    # Create accessor (getter) method for color
    def get_color(self):
        return self.__color
    
    # Create mutator (setter) method for color
    def set_color(self, color):
        self.__color = color