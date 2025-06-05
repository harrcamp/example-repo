"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:

# Initialise the instance variables for each email.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# Initialize an empty list called Inbox to store and access email objects
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    emails_to_create = [
        Email(
            "hpc710@gmail.com", 
            "We'd like to offer you the job...", 
            " Hello Mr. Campbell, \n We are writing to inform you that we would like you to be our new employee. \n Sincerely, Company"
        ), 
        Email(
            "mereswartz18@gmail.com",
            "Congrats on closing the Deal!", 
            "Hi Meredith, \n Thanks for your time and patience with the client, it really paid off! Big win for Salesforce! \n Best, Bossman"
        ),
        Email(
            "mgcampbell18@gmail.com", 
            "You fixed our kid", 
            "Dear Ms. Campbell, \n Our Billy was illiterate before he met you. You're a life saver. \n Mr. and Mrs. Winnebego."
        )
    ]

    # Append each Email object directly
    inbox.extend(emails_to_create)

# Call the function populate_inbox to add email objects to empty inbox list
populate_inbox()

def list_emails():
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for i, Email in enumerate(inbox):
        print(f"\n[{i}] {Email.subject_line}")
    print()

# Call the function to "open the inbox" and show emails with index values
list_emails()


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    # Request user to select an email to read
    try:
        email = inbox[index]
    except IndexError:
        print("No email exists at that index")
        return
    
    # Display email fields
    print("\n-------- MESSAGE-------------")
    print(f"From:      {email.email_address}")
    print(f"Subject:   {email.subject_line}")
    print(f"Content:\n{email.email_content}")
    print("----------------------------\n")

    email.has_been_read = True
    print(f"Email from {email.email_address} marked as read. \n")

def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    pass

# --- Email Program --- #

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.

menu_text = """
Would you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

Enter selection: """
while True:
    raw = input(menu_text).strip()
    if raw not in ("1","2","3"):
        print("Invalid selection. Please enter 1, 2 or 3.")
        continue
    user_choice = int(raw)

    if user_choice == 1:
        # Add logic here to read an email
        i = int(input("\tEmail Index: "))
        read_email(i)

    elif user_choice == 2:
        # Add logic here to view unread emails
        found_unread = False
        
        for email in inbox:
            if not email.has_been_read:
                print(f"\n{email.subject_line}")
                found_unread = True

        if not found_unread:
            print("\nNo unread emails.")

    elif user_choice == 3:
        # Add logic here to quit application.
        print("\nGood-bye!""\n")
        exit()

    else:
        print("Oops - incorrect input.")
