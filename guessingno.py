import random

print("Welcome to the Number Guessing Game!")

n = random.randint(0, 100)

attempts = 5
while attempts > 0:
    print("You have", attempts, "attempts to guess the number.")

    guessed = False
    try:
        g = int(input("Guess a number between 0 and 100 or if you want to quit, enter -1: "))

        if g == -1:
            print("Bye! Thanks for playing!")
            break

        if g < n:
            attempts -= 1
            print("That's a low guess. Try again!")

        elif g > n:
            attempts -= 1
            print("That's a high guess. Try again!")

        else:
            guessed = True
            print("Congratulations! You've guessed the number with", 5 - attempts + 1, "attempts!")
            break

    except ValueError:
        attempts -= 1
        print("Invalid input. Please enter a whole number.")

    if attempts > 0 and not guessed:
        print("You have", attempts, "attempts left.")

    if attempts == 0:
        print("You've run out of attempts. The number was", n)
        break