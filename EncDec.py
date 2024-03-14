import random
import string
import time
from os import system, name

# Print program title
print("\n\t\tThe ** MAHAN ** ENCRYPTION and DECRYPTION Program\n ")

while True:
    # Print increasing pattern of numbers
    for i in range(1, 7):
        print(" 01" * i)
    
    # Print menu options
    print("\nChoose Your Option: \n\t1) Encryption & Decryption\n\t2) Generate a password \n\t3) Timer\n\t4) Exit\n")
    
    # Print decreasing pattern of numbers
    for i in reversed(range(1, 7)):
        print(" 01" * i)
    
    # Get user input for choice
    x = input("\nPlease Enter Your Choice: ")
    
    if x == "1":
        while True:
            # Print encryption and decryption options
            print("Options: \n\t1) Encryption\n\t2) Decryption\n\t3) Back")
            
            # Get user input for encryption/decryption choice
            ed = input("Choose Your option: ")
            
            if ed == "1":
                while True:
                    # Clear the console screen
                    if name == "nt":
                        system("cls")
                    else:
                        system("clear")
                    
                    # Print encryption title
                    print("\n\t\t\t\t$$$$$  Encryption  $$$$$")
                    
                    # Get user input for text to encrypt
                    Text = input("Enter Your Text: ")
                    
                    # Encrypt the text
                    encrypted_Text = ""
                    for c in Text:
                        y = (ord(c) + 55) * 2
                        encrypted_Text += chr(y)
                    
                    # Print the encrypted text
                    print("Your Encrypted text is : ", encrypted_Text)
                    
                    # Ask user if they want to continue
                    f = input("Do you want to continue? (Y/N): ")
                    if "y" in f.lower():
                        continue
                    elif "n" in f.lower():
                        break
            elif ed == "2":
                while True:
                    # Clear the console screen
                    if name == "nt":
                        system("cls")
                    else:
                        system("clear")
                    
                    # Print decryption title
                    print("\n\t\t\t\t$$$$$  Decryption  $$$$$")
                    
                    # Get user input for encrypted text to decrypt
                    encrypted_Text = input("Enter Your Encrypted Text: ")
                    
                    # Decrypt the text
                    Text = ""
                    for c in encrypted_Text:
                        y = (ord(c)) // 2 - 55
                        Text += chr(y)
                    
                    # Print the decrypted text
                    print("Your text is : ", Text)
                    
                    # Ask user if they want to continue
                    f = input("Do you want to continue? (Y/N): ")
                    if "y" in f.lower():
                        continue
                    elif "n" in f.lower():
                        break
            elif ed == "3":
                break
    elif x == "2":
        letters_lower = string.ascii_lowercase
        numbers = string.digits
        symbols = string.punctuation
        letters_upper = string.ascii_uppercase
        all_ch = letters_lower + letters_upper + numbers + symbols
        while True:
            # Print password options
            print("Choose an option: \n\t 1)Create a Password\n\t 2)Back")
            
            # Get user input for password option
            x = input("Enter your option number: ")
            
            if x == "1":
                # Get user input for password length
                lenth = int(input("Enter the length of the password: "))
                
                # Generate a random password
                password = "".join(random.sample(all_ch, lenth))
                
                # Print the generated password
                print("Your password is: ", password)
            
            if x == "2":
                break
    elif x == "3":
        # Get user input for timer duration
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        
        # Calculate total time in seconds
        total = hours * 60 * 60 + minutes * 60 + seconds
        
        while total >= 1:
            # Clear the console screen
            if name == "nt":
                system("cls")
            else:
                system("clear")
            
            # Print remaining time
            print(total)
            
            # Decrease total time by 1 second
            total -= 1
            
            # Wait for 1 second
            time.sleep(1)
        
        # Print timer ended message
        else:
            print("timer ended!")
    elif x == "4":
        # Print exit message
        print("\n\t\t\t\tExit   |||||   Thank you for using")
        break
    else:
        # Print invalid choice message
        print("*" * 10)
        print("Your Choice is Invalid")
        print("*" * 10)
