

class Wolf:

    # Class variable 
    classification = "canine"
    habitat = "forest"
    is_sleeping = False # Defaults to being awake initially

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method that returns the sleep state of the wolf
    def show_sleep_state(self):
        if self.is_sleeping == False:
            return self.name + " is awake"
        else:
            return self.name + " is sleeping"
    
    # Method to put wolf to sleep (self needs to be passed as arguement)
    # so that all of the properties are available to the method)
    def bed_time(self):
        self.is_sleeping = True

    # Method to wake up wolf (self needs to be passed as arguement
    # so that all of the properties are available to the method)
    def wake_up(self):
        self.is_sleeping = False

# First object, provide instance variables for the contructor method
silver_tooth = Wolf("Silvertooth", 5)

# Initialise a wolf object and print the initial sleep
# state which is awake 
print(silver_tooth.show_sleep_state())

# Change sleep state to sleeping using do notation and then print new state
silver_tooth.is_sleeping = True
print(silver_tooth.show_sleep_state())

# Print out the instance variable 'name'
print(silver_tooth.name)

# Print out class variable 'havitat'
print(silver_tooth.habitat)

# Second object
lone_wolf = Wolf("Lone Wolf", 8)

# Print out instance variable 'name'
print(lone_wolf.name)

# Print classification (class variable) for new_wolf
print(lone_wolf.classification) # Output: canine



