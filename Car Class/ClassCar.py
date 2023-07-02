# Create a class named Car
class Car:
    # Create constructor that creates a car with the specified year model, make and speed
    def __init__(self, year_model, make, speed = 0):
        # Create instance variable 
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
