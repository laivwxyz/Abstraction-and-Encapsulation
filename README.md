# ![Screenshot (691)](https://github.com/laivwxyz/Abstraction-and-Encapsulation/assets/129714181/79a2cfff-1dbf-4b50-91ea-78a4396e97ca)

This repository contains solutions to three programming problems: `The Fan Class`, `Car Class`, and `Pet Class`.

# ~~~
##  The Fan Class
![Screenshot (680)](https://github.com/laivwxyz/Abstraction-and-Encapsulation/assets/129714181/da8cf1ae-b509-461c-9ef8-8808a9bf8d5d)

The `Fan` class represents a fan and provides methods to control its properties such as speed, on/off state, radius, and color.

### Class Description

The `Fan` class has the following components:

- Constants: `SLOW`, `MEDIUM`, and `FAST` representing fan speeds.
  
- Attributes: `speed` (private), `on` (private), `radius` (private), and `color` (private).
  
- Methods: Accessor and mutator methods for the attributes, and a constructor to create a `Fan` object with default values.
  
### Test Program

The test program, `TestFan.py`, creates two `Fan` objects and displays their properties.

# ~~~
## Car Class
![Screenshot (688)](https://github.com/laivwxyz/Abstraction-and-Encapsulation/assets/129714181/fe0183bb-612e-4499-a450-f3e55a930dbb)


The `Car` class represents a car and provides methods to control its properties such as year model, make, and speed.

### Class Description

The Car class has the following components:

- Attributes: `__year_model` (private), `__make` (private), and `__speed` (private).

- Methods: `accelerate()`, `brake()`, and `get_speed()`.

### Test Program

The test program, `TestCar.py`, creates a `Car` object, calls the `accelerate()` method five times, displays the current speed after each call, calls the `brake()` method five times, and displays the current speed after each call.

# ~~~
## Pet Class
![Screenshot (690)](https://github.com/laivwxyz/Abstraction-and-Encapsulation/assets/129714181/6ea4f8b6-940a-4730-9e53-3292e8307e82)

The `Pet` class represents a pet and provides methods to set and retrieve its attributes such as name, animal type, and age.

### Class Description

The `Pet` class has the following components:

- Attributes: `__name` (private), `__animal_type` (private), and `__age` (private).

- Methods: `set_name()`, `set_animal_type()`, `set_age()`, `get_name()`, `get_animal_type()`, and `get_age()`.

### Test Program

The test program prompts the user to enter the name, type, and age of their pet, stores the input as the object's attributes, and displays the pet's information.

## Contribute

Contributions are always welcome! Please read the [contribution guidelines](https://github.com/matiassingers/awesome-readme/blob/master/contributing.md) first.
