import os
import pyjokes as jokes

print("Welcome to the Joke App!")

while True:
    try:
        signin = input("Please select from \n1.Register\n2.Login\n Enter your choice: ")

        if signin == "1" or signin == "Register":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            existing_usernames = set()
            if os.path.exists("users.txt"):
                with open("users.txt", "r") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            existing_usernames.add(line.split(",")[0])

            while username in existing_usernames:
                print("That username is already taken. Please enter a different username.")
                username = input("Enter your username: ")

            print("Registration successful!")
            with open("users.txt", "a") as f:
                f.write(username + "," + password + "\n")

            print("Here's a joke for you: ")
            print(jokes.get_joke())

        elif signin == "2" or signin == "Login":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            login_success = False
            if os.path.exists("users.txt"):
                with open("users.txt", "r") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            stored_username, stored_password = line.split(",")
                            if username == stored_username and password == stored_password:
                                login_success = True
                                break

            if not login_success:
                print("Invalid username or password.")
                continue

            print("Login successful!")
            print("Here's a joke for you: ")
            print(jokes.get_joke())
        
        elif signin not in ["1", "2", "Register", "Login"]:
            print("Invalid choice. Please enter from 1 or 2 or Register or Login: ")
            continue
        
        else:
            print("No users registered yet. Please try from 1 or Register.")
            continue
        
        while True:
            ask = input("Do you want to see another joke? (yes/no): ")
            if ask.lower() == "yes":
                print(jokes.get_joke())

            elif ask.lower() == "no":
                print("Goodbye!")
                break
        break

    except ValueError:
        print("Invalid input. Please enter a valid choice.")
        continue