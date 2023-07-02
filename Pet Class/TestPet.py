# Add designs to the program
from pyfiglet import Figlet
from termcolor import colored

# Import class Pet from ClassPet.py
from ClassPet import Pet

f = Figlet(font='serifcap', width = 145)
print(colored(f.renderText("              Program output: "), 'light_red'))

def test_pet():
    # Create an object of the Pet class
    # Ask the user to enter pet details
    name = (input(" " * 50 + "\033[96mEnter the name of your pet: \033[0m"))
    print()
    animal_type = input(" " * 50 + "\033[96mEnter the type of animal: \033[0m")
    print()
    age = input(" " * 50 + "\033[96mEnter the age of your pet: \033[0m")
    print()

    pet = Pet(name, animal_type, age)

    # Display the pet details 
    print()
    print(" " * 50, "\033[93m(", " " * 5, "PET DETAILS:", " " * 5, "\033[93m)")
    print()
    print(" " * 56, "\033[95mName:", "\033[0m", pet.get_name())
    print()
    print(" " * 56, "\033[95mAnimal Type:", "\033[0m", pet.get_animal_type())
    print()
    print(" " * 56, "\033[95mAge:", "\033[0m", pet.get_age(), "years old")
    print()
    
# Run the test_pet function
test_pet()