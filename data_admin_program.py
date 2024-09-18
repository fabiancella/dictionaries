import random

print("Welcome to the Database Admin App")

username_password = {
    "bob123": "monkey123",
    "luke989": "dude123",
    "davidantas": "fatboy123",
}

username = input("\nPlease input username: ")
password = input("Please input password: ")

if username in username_password and username_password[username] == password:
    print("\nHello " + username + ", you are logged in.")

else:
    print("\nSorry, wrong username or password.\nPlease try again.")
    exit()

choice = input("Would you like to change your password (y/n): ").lower().strip()

if "y" in choice:
    new_password = input("\nWhat would you like this new password to be? ")
    username_password[username] = new_password
    print(username, "your new is " + new_password + ".")
else: print("\nOkay have a good day"),

# new_password = input("\nWhat would you like this new password to be? ")
# if username in username_password:
#     username_password[username] = new_password
#     print(username, "your new is", new_password, ".")


