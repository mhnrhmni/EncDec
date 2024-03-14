import random
import string
import time
from os import system, name
print("\n\t\tThe ** MAHAN ** ENCRYPTION and DECRYPTION Program\n ")
while True:
    for i in range(1, 7):
        print(" 01" * i)
    print("\nChoose Your Option: \n\t1) Encryption & Decryption\n\t2) Generate a password \n\t3) Timer\n\t4) Exit\n")
    for i in reversed(range(1, 7)):
        print(" 01" * i)
    x = input("\nPlease Enter Your Choice: ")
    if x == "1":
        while True:
            print("Options: \n\t1) Encryption\n\t2) Decryption\n\t3) Back")
            ed = input("Choose Your option: ")
            if ed == "1":
                while True:
                    if name == "nt":
                        system("cls")
                    else:
                        system("clear")
                    print("\n\t\t\t\t$$$$$  Encryption  $$$$$")
                    Text = input("Enter Your Text: ")
                    encrypted_Text = ""
                    for c in Text:
                        y = (ord(c) + 55) * 2
                        encrypted_Text += chr(y)
                    print("Your Encrypted text is : ", encrypted_Text)
                    f = input("Do you want to continue? (Y/N): ")
                    if "y" in f.lower():
                        continue
                    elif "n" in f.lower():
                        break
            elif ed == "2":
                while True:
                    if name == "nt":
                        system("cls")
                    else:
                        system("clear")
                    print("\n\t\t\t\t$$$$$  Decryption  $$$$$")
                    encrypted_Text = input("Enter Your Encrypted Text: ")
                    Text = ""
                    for c in encrypted_Text:
                        y = (ord(c)) // 2 - 55
                        Text += chr(y)
                    print("Your text is : ", Text)
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
            print("Choose an option: \n\t 1)Create a Password\n\t 2)Back")
            x = input("Enter your option number: ")
            if x == "1":
                lenth = int(input("Enter the length of the password: "))
                password = "".join(random.sample(all_ch, lenth))
                print("Your password is: ", password)
            if x == "2":
                break
    elif x == "3":
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        total = hours * 60 * 60 + minutes * 60 + seconds
        while total >= 1:
            if name == "nt":
                system("cls")
            else:
                system("clear")
            print(total)
            total -= 1
            time.sleep(1)
        else:
            print("timer ended!")
    elif x == "4":
        print("\n\t\t\t\tExit   |||||   Thank you for using")
        break
    else:
        print("*" * 10)
        print("Your Choice is Invalid")
        print("*" * 10)
        