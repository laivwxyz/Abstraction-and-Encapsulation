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
