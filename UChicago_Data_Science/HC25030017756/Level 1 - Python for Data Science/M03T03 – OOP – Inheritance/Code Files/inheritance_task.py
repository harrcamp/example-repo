class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Class attribute for head office location
    head_office_location = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
     
    # Method to print the head office location Cape Town
    def head_office(self):
        print("The head office location is", self.head_office_location)


# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()
course.head_office()

class OOPCourse(Course):
    def __init__(self, 
                 description="OOPFundamentals", trainer="Mr Anon A. Mouse", course_id="#12345"):
        super().__init__()
        self.description = description
        self.trainer = trainer
        self.course_id = course_id

    def course_details(self):
        print("The course is about", self.description)

    def trainer_details(self):
        print("The trainer for this course is", self.trainer)

    def show_course_ID(self):
        print("The course ID is", self.course_id)

course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_ID()
