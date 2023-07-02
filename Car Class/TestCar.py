# Import class Car from ClassCar.py
from ClassCar import Car

def test_car():
    # Create a Car object
    car = Car(2022, "Toyota", 0)

    # Call the accelerate method five times and display the current speed
    print("Accelerate")
    print("Car year model: ", car.get_year_model())
    print("Car is made of: ", car.get_make())
    print("Speed")
    for _ in range(5):
        car.accelerate()
        print("Current speed:", car.get_speed())
