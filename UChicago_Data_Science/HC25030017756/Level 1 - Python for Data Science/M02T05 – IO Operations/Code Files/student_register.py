# Ask the user how many students are registering 
num_students = int(input("How many students are registering for the exam?: "))

file_path = '/Users/harrycampbell/Documents/UChicago_Data_Science/HC25030017756/Level 1 - Python for Data Science/M02T05 – IO Operations/Code Files'
# Request entry for student ID for the number of students

with open("/Users/harrycampbell/Documents/UChicago_Data_Science/HC25030017756/Level 1 - Python for Data Science/M02T05 – IO Operations/Code Files/reg_form.txt", "w") as reg_form:
    for student in range(num_students):
        student_IDs = input("What is the student's ID number?:  ")
        reg_form.write(student_IDs + "  _ _ _ _ _ _ _ _ _ _ _" + "\n")
    print("Looks like everyone's on the sheet.")

    