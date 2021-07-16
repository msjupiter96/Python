"""
File: password_gen.py
Purpose: This program generates a random password based on user specifications. The program runs until the user selects to to option to end it.
Author: msjupiter96

"""

"""
Algorithm:
a. Ask user for password length. Validate input is integer
b. Ask if they want to use uppercase and/or lowercase letters. Validate user chooses atleast 1 option
c. Ask if they want to use numbers and/or special characters. Validate user chose atleast 1 option before
e. Generate password based on user-specifications
f. Output generated password, ask if use wants to create another one

"""
import string
import random

# Main function
def main():
    program_status = True
    # Program runs until user ends it
    while program_status == True:
        pass_length = int(input("Please enter the password length (must be an integer): "))
        # True and False based user inputs
        choice1 = input("Use uppercase letters?(Y/N): ")
        choice2 = input("Use lowercase letters?(Y/N): ")
        choice3 = input("Use numbers?(Y/N): ")
        choice4 = input("Use special characters?(Y/N): ")


        # Check for uppercase selection
        if choice1 == 'Y' or choice1 == 'y':
            uppercase_status = True
        elif choice1 == 'N' or choice1 == 'n':
            uppercase_status = False
        else:
            print("Invalid Entry")
        # Check for lowercase selection
        if choice2 == 'Y' or choice2 == 'y':
            lowercase_status = True
        elif choice2 == 'N' or choice2 == 'n':
            lowercase_status = False
        else:
            print("Invalid Entry")
        # Check for numbers
        if choice3 == 'Y' or choice3 == 'y':
            number_status = True
        elif choice3 == 'N' or choice3 == 'n':
            number_status = False
        else:
            print("Invalid Entry")
        # Check for special chars
        if choice4 == 'Y' or choice4 == 'y':
            specialchar_status = True
        elif choice4 == 'N' or choice4 == 'n':
            specialchar_status = False
        else:
            print("Invalid Entry")

        # Make sure atleast 1 option is selected
        if uppercase_status == True or lowercase_status == True or number_status == True or specialchar_status == True:
            # Generate password
            result = password_generate(pass_length, uppercase_status, lowercase_status, specialchar_status)
            # Print the randomly generated password
            print("Random Password:", result)
            program_continue = input("Run the generator again?(Y/N): ")
            if program_continue == 'Y' or program_continue == 'y':
                continue
            elif program_continue == 'N' or program_continue == 'n':
                program_status = False
            else:
                print("Invalid Entry")
                continue
            
        
        

# Function to generate password
def password_generate(length, uppercase, lowercase, special):
    # Variable to store string of random characters and numbers
    randomizer = ""
    # Stores final generated pass
    generated_pass = ""
    
    if uppercase == True:
        uppercase_letters = string.ascii_uppercase # create string of uppercase letters
        randomizer += uppercase_letters
    if lowercase == True:
        lowercase_letters = string.ascii_lowercase # create string of lowercase letters
        randomizer += lowercase_letters
    if special == True:
        special_chars = string.punctuation # create string of special chars
        randomizer += special_chars



    # Create password based on specifications
    for i in range(length):
        generated_pass += random.choice(randomizer)

    return generated_pass
        
    


# Run the program
main()
