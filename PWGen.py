"""
Generates a password based on user input.

The function prompts the user to enter the desired password length.
If the length is valid (between 4 and 32 characters), a random password
is generated and added to the 'senhas' list. The generated password is
then displayed to the user.

If the length is invalid, an error message is displayed and the user is
prompted again.

The 'view_passwords' function displays all the passwords generated so far.

The 'main' function displays a menu with the following options:
1. Generate password
2. View passwords
3. Exit

The 'generate_password' function generates a random password based on the given length.
The 'view_passwords' function displays all the passwords generated so far.
The 'main' function is the entry point of the program and displays the menu options.

Author: BrunoMagno
"""

import os
import random
import sys
import time
import string
import csv

# List of valid characters
characters = string.ascii_letters + string.digits + string.punctuation.replace(" ", "")

# File to store the passwords
password_file = "passwords.csv"

def generate_password():
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        length = int(input("Enter the password length (4-32): "))

        if length < 4 or length > 32:
            print("Invalid length. The password must be between 4 and 32 characters.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            generate_password()
        else:
            password = "".join(random.choice(characters) for _ in range(length))

            with open(password_file, 'a', newline='') as csvfile:
                password_writer = csv.writer(csvfile)
                password_writer.writerow([password])

            print("Password: ", password)
            print("Password generated successfully!")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
    except ValueError:
        print("Invalid value")
        time.sleep(2)
        generate_password()

def view_passwords():
    os.system('cls' if os.name == 'nt' else 'clear')
    passwords = [] 

    # Read passwords from the CSV file
    with open(password_file, 'r') as csvfile:
        password_reader = csv.reader(csvfile)
        for row in password_reader:
            passwords.append(row[0])  

    if not passwords:
        print("No passwords generated yet.")
        time.sleep(2)
        main()
    else:
        print("Generated passwords:")
        print("")
        time.sleep(1)
        for i, password in enumerate(passwords, start=1):
            print(f"{i}. {password}")
        input("Press enter to go back...")
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("    Password Generator  ")
    
    time.sleep(1)
    print("")
    print("1. Generate password")
    print("2. View passwords")
    print("3. Exit")
    print("")

    
    try:
        opcao = int(input("Enter the desired option: "))
        
        match opcao:
            case 1:
                generate_password()
            case 2:
                view_passwords()
            case 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Thank you for using the Password Generator!")
                print("By BrunoMagno")
                time.sleep(2)
                sys.exit()
            case default:
                print("Invalid option.")
                time.sleep(1)
                main()
    except ValueError:
        print("Invalid value")
        time.sleep(2)
        main()
        
main()