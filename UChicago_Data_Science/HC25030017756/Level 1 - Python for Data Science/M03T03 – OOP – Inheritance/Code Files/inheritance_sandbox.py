# Parent class for a car which we can extend to a subclass
class Car:
    # class variable for whether the engine is running or not
    is_running = False
    
    # Constructor that allows us to set the make and model
    # as instance variables
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Method to start the engine
    def start_car(self):
        self.is_running = True
        
    # Method to turn off the engine
    def turn_off_car(self):
        self.is_running = False

    # Method to print the make and model
    def show_make_and_model(self):
        print(f"This vehicle is a {self.make} {self.model}")


# We are inheriting all of the attributes and methods
# from the Car class by passing it as an arguement to 
# the PickupTruck class
        
class PickupTruck(Car):
    # This is an additional class variable that is specific
    # to the PickupTruck class
    is_loaded = False

# Method to load the truck
    def load(self):
        self.is_loaded = True

    # Method to remove the load from the truck
        def unload(self):
            self.is_loaded = False


# Create a pickup truck object
pickup_truck_1 = PickupTruck("Toyota", "Hilux")

# Call the load method that we created in the subclass
# This changes the variable from False to True
pickup_truck_1.load()

# Call the start_car method inherited fomr the parent class
pickup_truck_1.start_car()

# Print out to values so that we can see that both
# of the above methods worked
print(pickup_truck_1.is_running)
print(pickup_truck_1.is_loaded)

# Call another method that was inherited from the parent class
pickup_truck_1.show_make_and_model()

#___________________________!!!!!!!!!!_________________________

# Define parent class
class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

# Define subclass
class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model

# Create a Laptop object
thinkpad = Laptop('Lenovo', 16, 512, 'Thinkpad')

# Print Laptop's features
print('Computer make:', thinkpad.computer)
print('Computer model:', thinkpad.model)
print(f"This computer has {thinkpad.ram} GB of RAM.")
print(f"This compuer has {thinkpad.ssd} GB of SSD storage.")


#___________________________!!!!!!!!!!_________________________

# Parent class
class Father():
    def transport(self):
        print("The transport used is a car")
# Subclass
class Son(Father):
    pass

son_1 = Son()
# This will output "The transport used is a car"
# becuase it is using the inherited method from the father class
son_1.transport()

##________ OR ## override the transport() method in the subclass 
#so that the transport used by the son is "bicycle"

# Parent class
class Father():
    def transport(self):
        print("The transport used is a car")

# Subclass 
class Son(Father):
    def transport(self):
        print("Son is riding a bicycle")

son_1 = Son()
# This will output "The transport used is a bicycle"
# because the inherited method is bein overridden
# by the Son subclass
son_1.transport()