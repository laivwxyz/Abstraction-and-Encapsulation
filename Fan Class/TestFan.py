# Add designs to the program
from pyfiglet import Figlet
from termcolor import colored

# import class Fan from ClassFan.py
from ClassFan import Fan

f = Figlet(font='serifcap', width = 140)
print(colored(f.renderText("Program output: "), 'light_cyan'))

def test_fan():
    # Create the first Fan object
    fan1 = Fan()
    fan1.get_speed()
    fan1.set_speed(Fan.FAST)
    fan1.get_on()
    fan1.set_on(True)
    fan1.get_radius()
    fan1.set_radius(10)
    fan1.get_color()
    fan1.set_color("Yellow")

    # Create the second Fan object
    fan2 = Fan()
    fan2.get_speed()
    fan2.set_speed(Fan.MEDIUM)
    fan2.get_on()
    fan2.set_on(False)
    fan2.get_radius()
    fan2.set_radius(5)
    fan2.get_color()
    fan2.set_color("Blue")

    # Display the First Fan information
    print(" " * 25, "\033[92m<", " " * 5, "First Fan", " " * 5, "\033[92m>")
    print()
    print(" " * 30, "\033[93mSpeed:" , "\033[0m", fan1.get_speed())
    print(" " * 30, "\033[93mRadius:" , "\033[0m", fan1.get_radius())
    print(" " * 30, "\033[93mColor:" , "\033[0m", fan1.get_color())
    print(" " * 30, "\033[93mOn:", "\033[0m", fan1.get_on())
    print()
    print()

    # Display the Second Fan information
    print(" " * 25, "\033[92m<", " " * 5, "Second Fan", " " * 5, "\033[92m>")
    print()
    print(" " * 30, "\033[93mSpeed:" , "\033[0m", fan2.get_speed())
    print(" " * 30, "\033[93mRadius:" , "\033[0m", fan2.get_radius())
    print(" " * 30, "\033[93mColor:" , "\033[0m", fan2.get_color())
    print(" " * 30, "\033[93mOn:", "\033[0m", fan2.get_on())
    print()
    print()

# Run the test_fan function
test_fan()