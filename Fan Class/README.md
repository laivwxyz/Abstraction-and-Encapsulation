![Screenshot (680)](https://github.com/laivwxyz/Abstraction-and-Encapsulation/assets/129714181/4aade213-c9fd-44f8-910c-6e6c723d8825)

The `Fan` class represents a fan and provides methods to control its properties such as speed, on/off state, radius, and color.

## GETTING STARTED

### PREREQUISITES

To run this script, you need to have Python installed on your system.

## Class Description

The `Fan` class has the following components:

### Constants

- `SLOW`, `MEDIUM`, and `FAST`: Constants representing the fan speed with values 1, 2, and 3, respectively.

### Attributes

- `speed` (private): An integer specifying the speed of the fan.

- `on` (private): A boolean indicating whether the fan is on or off.

- `radius` (private): A float specifying the radius of the fan.

- `color` (private): A string specifying the color of the fan.

### Methods

The Fan class provides the following methods:

- `__init__(self, speed=1, radius=5, color='blue', on=False)`: Constructor that initializes a Fan object with the specified speed, radius, color, and on state.

- Getter and setter methods for all four data fields: `get_speed(), set_speed(speed), get_radius(), set_radius(radius), get_color(), set_color(color), is_on(), set_on(on)`.

- `__str__(self) -> str`: Returns a string representation of the Fan object.

- `turn_on()`: Turns on the fan.

- `turn_off()`: Turns off the fan.

## Test Program

The test program, `TestFan.py`, demonstrates the usage of the `Fan` class by creating two `Fan` objects with different properties and displaying their attributes.

### Sample Output

The output of the test program will display the speed, radius, color, and on properties of the `Fan` objects.

![Screenshot (678)](https://github.com/laivwxyz/Abstraction-and-Encapsulation/assets/129714181/277eef7d-479c-4e22-b0ea-e1e722871354)

## Running the Program

- Clone the repository or download the files `ClassFan.py` and `TestFan.py`.

- Make sure you have Python installed on your system.

- Open your terminal or command prompt and navigate to the directory where the files are located.

- Run the test program by executing the command: python `TestFan.py`.

- The output will be displayed in the terminal.

## CONTRIBUTE

Contributions are always welcome! Please read the [contribution guidelines](https://github.com/matiassingers/awesome-readme/blob/master/contributing.md) first.
