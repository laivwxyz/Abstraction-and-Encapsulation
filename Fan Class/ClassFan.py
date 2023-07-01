# Create a class named Fan 
class Fan:
    # Create constant to denote the fan speed 
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Create constructor that creates a fan with the specified speed, radius, color and on
    def __init__(self, speed = SLOW, radius = 5, color = 'blue', on = False):
        # Create instance variable 
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
