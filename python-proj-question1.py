###1) Create a simple Python program application that does the following:

    # Prints "Hello User!"

    # Then asks "What is your name?"

    # Then responds "Hello <user's name>"

    # Then asks: "What is your year of birth?"

    # Then ask: "Do you know how to drive?"

    # Then ask: "How old were you when you got your driving license" if the user replied "Yes" to the above question

    # Then outputs: "You got your driving license in <year> and you have been driving for <x> years" 

    # Then outputs: "You are <age> years old now but you still can't drive. You were supposed to get your license in <year>,<x> years ago at the age of 30 at the latest"
    # If the user replied "No" and is over the age of 30

    # Then outputs: "You are <age> years old now and you should work on getting your driving license before you turn 30. You have <x> years to go until the year <year>" 
    # If the user replied "No" and is under the age of 30
from datetime import datetime

    # Print the initial greeting
print("Hello User!")
   
    # Ask for the user's name and greet them
name = input("What is your name? ")
print(f"Hello {name}!")
   
    # Ask for the user's year of birth
birth_year = int(input("What is your year of birth? "))
   
    # Calculate the current year and the user's age
current_year = datetime.now().year
age = current_year - birth_year
   
    # Ask if the user knows how to drive
knows_to_drive = input("Do you know how to drive? (Yes/No) ").lower()


if knows_to_drive == "yes":
        # Ask for the age at which they got their driving license
        license_age = int(input("How old were you when you got your driving license? "))
       
        # Calculate the year they got their driving license
        license_year = birth_year + license_age
        years_driving = current_year - license_year
       
        # Output the information about when they got their license and how long they've been driving
        print(f"You got your driving license in {license_year} and you have been driving for {years_driving} years.")
   
elif knows_to_drive == "no":
        if age > 30:
            # If the user is over 30 and does not know how to drive
            print(f"You are {age} years old now but you still can't drive. You were supposed to get your license in {current_year - 30}, {age - 30} years ago at the age of 30 at the latest.")
        else:
            # If the user is under 30 and does not know how to drive
            print(f"You are {age} years old now and you should work on getting your driving license before you turn 30. You have {30 - age} years to go until the year {current_year + (30 - age)}.")
else:
        print("Invalid response. Please enter 'Yes' or 'No'.")



