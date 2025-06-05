# request user input for the following details
name = str(input("What is your name?: "))
age = int(input("How old are you?: "))
hair_color = str(input("What color is your hair?: "))
eye_color = str(input("What color are your eyes?: "))

# Define Adult class
class Adult():
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

# Method stating this person can drive
    def can_drive(self):
        print(f"{name} is old enough to drive.")

# Define Child class that inherits the same attributes
class Child(Adult):
    def __init__(self, name, age, hair_color, eye_color):
        super().__init__(name, age, hair_color, eye_color)

# Method stating that this person is not old enough to drive
    def can_drive(self):
        print(f"{name} is not old enough to drive.")

# Initiate each class based on age
if age >= 18:
    person_1 = Adult(name, age, hair_color, eye_color)
else:
    person_1 = Child(name, age, hair_color, eye_color)

# call the method to state whether the person can drive or not
person_1.can_drive()