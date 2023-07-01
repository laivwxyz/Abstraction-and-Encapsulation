# import class Fan from ClassFan.py
from ClassFan import Fan

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
    print("First Fan")
    print("Speed:" , fan1.get_speed())
    print("Radius:" , fan1.get_radius())
    print("Color:" , fan1.get_color())
    print("On:", fan1.get_on())