import random

def number_guessing_game():
    """A number guessing game with a limit of 4 attempts."""

    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    max_attempts = 4

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return  # Exit the function if the guess is correct

            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"You've run out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()