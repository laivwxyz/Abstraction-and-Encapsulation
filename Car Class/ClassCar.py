# Create a class named Car
class Car:
    # Create constructor that creates a car with the specified year model, make and speed
    def __init__(self, year_model, make, speed = 0):
        # Create instance variable 
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    # Create accessor (getter) method for year model
    def get_year_model(self):
        return self.__year_model
    
    # Create mutator (setter) method for year model
    def set_year_model(self, year_model): 
        self.__year_model = year_model

    # Create accessor (getter) method for make
    def get_make(self):
        return self.__make
    
    # Create mutator (setter) method for make
    def set_make(self, make):
        self.__make = make 
