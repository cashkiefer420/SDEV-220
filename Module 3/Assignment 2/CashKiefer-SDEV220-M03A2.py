''' 
Author: Cash Kiefer
File Name: CashKiefer-SDEV220-M03A2.py
Description: This program will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the data.
'''

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type  # Store the type of vehicle (e.g., car, truck, etc.)

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")  # Set vehicle type to "car"
        self.year = year  # Store the car's year
        self.make = make  # Store the car's make
        self.model = model  # Store the car's model
        self.doors = doors  # Store the number of doors (2 or 4)
        self.roof = roof  # Store the type of roof (solid or sun roof)

    def display_info(self):
        """Prints the car details in a readable format."""
        print("\nVehicle Information:")
        print(f"  Vehicle type: {self.vehicle_type}")
        print(f"  Year: {self.year}")
        print(f"  Make: {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Number of doors: {self.doors}")
        print(f"  Type of roof: {self.roof}")

# Collect user input
year = input("Enter the car's year: ")
make = input("Enter the car's make: ")
model = input("Enter the car's model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Create an Automobile object
car = Automobile(year, make, model, doors, roof)

# Display the information
car.display_info()
