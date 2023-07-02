# Import class Pet from ClassPet.py
from ClassPet import Pet

def test_pet():
    # Create an object of the Pet class
    # Ask the user to enter pet details
    name = input("Enter the name of your pet: ")
    animal_type = input("Enter the type of animal: ")
    age = input("Enter the age of your pet: ")

    pet = Pet(name, animal_type, age)

    # Display the pet details 
    print("Pet Details:")
    print("Name:", pet.get_name())
    print("Animal Type:", pet.get_animal_type())
    print("Age:", pet.get_age())
    
# Run the test_pet function
test_pet()