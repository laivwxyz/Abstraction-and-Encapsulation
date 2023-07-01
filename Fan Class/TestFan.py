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