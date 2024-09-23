import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: Make a guess: ")

        # Check if input is a number
        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)  # Convert input to an integer
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it! The number was {secret_number}.")
            break
    else:
        print(f"Sorry! You've used all your attempts. The number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
