class Vehicle():
    def __init__(self):
        self.type = input("Please enter the type of vehicle: ")  
            
class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = input("Please enter the year: ")
        self.make = input("Please enter the make: ")
        self.model = input("Please enter the model: ")
        self.doors = input("Please enter the number of doors: ")
        self.roof = input("Please enter the type of roof: ")

    def displayInfo(self):
        print("\nType:", self.type, "\nYear:", self.year, "\nMake:", self.make, "\nModel:", self.model, "\nNumber of doors:", self.doors, "\nType of roof:", self.roof)

vehicle = Automobile()
print(vehicle.displayInfo())