# Add designs in the program
from pyfiglet import Figlet
from termcolor import colored

# Import class Car from ClassCar.py
from ClassCar import Car

f = Figlet(font='serifcap', width = 145)
print(colored(f.renderText("              Program output: "), 'light_yellow'))

def test_car():
    # Create a Car object
    car = Car(2022, "Toyota", 0)

    # Call the accelerate method five times and display the current speed
    print(" " * 55, "\033[96m(", " " * 5, "ACCELERATE", " " * 5, "\033[96m)")
    print()
    print(" " * 57, "\033[92mCar year model: ", "\033[0m", car.get_year_model())
    print(" " * 57, "\033[92mCar is made of: ", "\033[0m", car.get_make())
    print()
    print(" " * 62, "\033[95m<","Speed", "\033[95m>")
    print()
    for _ in range(5):
        car.accelerate()
        print(" " * 59, "\033[92mCurrent speed:", "\033[0m", car.get_speed())
        print()

    # Call the brake method five times and display the current speed
    print()
    print(" " * 57, "\033[96m(", " " * 5, "BRAKE", " " * 5, "\033[96m)")
    print()
    print(" " * 56, "\033[92mCar year model: ", "\033[0m", car.get_year_model())
    print(" " * 56, "\033[92mCar is made of: ", "\033[0m", car.get_make())
    print()
    print(" " * 63, "\033[95m<","Speed", "\033[95m>")
    print()
    for _ in range(5):
        car.brake()
        print(" " * 60, "\033[92mCurrent speed:", "\033[0m", car.get_speed())
        print()

# Run the test_fan function
test_car()