# Vehicle rental service.
class Vehicle:
    def __init__(self, make, model, year, rental_rate):
        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Rate: {self.rental_rate}")


class Car(Vehicle):
    def __init__(self, make, model, year, rental_rate, num_doors):
        super().__init__(make, model, year, rental_rate)
        self.num_doors = num_doors
        self.is_rented = False

    def rent_vehicle(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"The car {self.model} has been rented.")
        else:
            print(f"The car {self.model} is already rented.")

    def return_vehicle(self):
        if self.is_rented:
            self.is_rented = False
            print(f"The car {self.model} has been returned.")
        else:
            print(f"The car {self.model} was not rented.")

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}, Rented: {self.is_rented}")


class Bike(Vehicle):
    def __init__(self, make, model, year, rental_rate, bike_type):
        super().__init__(make, model, year, rental_rate)
        self.bike_type = bike_type
        self.is_rented = False

    def rent_vehicle(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"The bike {self.model} has been rented.")
        else:
            print(f"The bike {self.model} is already rented.")

    def return_vehicle(self):
        if self.is_rented:
            self.is_rented = False
            print(f"The bike {self.model} has been returned.")
        else:
            print(f"The bike {self.model} was not rented.")

    def display_info(self):
        super().display_info()
        print(f"Bike Type: {self.bike_type}, Rented: {self.is_rented}")


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rented_vehicles = []

    def rent_vehicle(self, vehicle):
        if not vehicle.is_rented:
            vehicle.rent_vehicle()
            self.rented_vehicles.append(vehicle)
            print(f"{self.name} has rented {vehicle.model}.")
        else:
            print(f"{vehicle.model} is already rented.")

    def return_vehicle(self, vehicle):
        if vehicle in self.rented_vehicles:
            vehicle.return_vehicle()
            self.rented_vehicles.remove(vehicle)
            print(f"{self.name} has returned {vehicle.model}.")
        else:
            print(f"{self.name} did not rent {vehicle.model}.")

    def display_customer_info(self):
        print(f"Customer Name: {self.name}, Customer ID: {self.customer_id}")
        print("Rented Vehicles:")
        for vehicle in self.rented_vehicles:
            vehicle.display_info()


class Employee(Customer):
    def __init__(self, name, customer_id, employee_id):
        super().__init__(name, customer_id)
        self.employee_id = employee_id
        self.managed_vehicles = []

    def add_vehicle(self, vehicle):
        self.managed_vehicles.append(vehicle)
        print(f"{vehicle.model} has been added to the fleet.")

    def remove_vehicle(self, vehicle):
        if vehicle in self.managed_vehicles:
            self.managed_vehicles.remove(vehicle)
            print(f"{vehicle.model} has been removed from the fleet.")
        else:
            print(f"{vehicle.model} is not in the fleet.")

    def display_customer_info(self):
        super().display_customer_info()
        print(f"Employee ID: {self.employee_id}")
        print("Managed Vehicles:")
        for vehicle in self.managed_vehicles:
            vehicle.display_info()


# Demonstration of functionality
if __name__ == "__main__":
    # Create vehicles
    car1 = Car("Toyota", "Camry", 2020, 50, 4)
    bike1 = Bike("Yamaha", "YZF", 2021, 15, "Sports")

    # Create customer and employee
    customer1 = Customer("Alice", 101)
    employee1 = Employee("Bob", 201, "E001")

    # Employee manages vehicles
    employee1.add_vehicle(car1)
    employee1.add_vehicle(bike1)

    # Display fleet managed by employee
    employee1.display_customer_info()

    # Customer rents a car
    customer1.rent_vehicle(car1)
    customer1.display_customer_info()

    # Customer tries to rent the same car again
    customer1.rent_vehicle(car1)

    # Customer returns the car
    customer1.return_vehicle(car1)
    customer1.display_customer_info()

    # Customer rents a bike
    customer1.rent_vehicle(bike1)
    customer1.display_customer_info()

    # Employee removes a vehicle from the fleet
    employee1.remove_vehicle(bike1)
    employee1.display_customer_info()
