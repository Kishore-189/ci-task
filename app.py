import random

# Function to start the game
def start_game():
    print("Welcome to the Number Guessing Game!")
    
    # Define the range for the random number
    lower = 1
    upper = 100
    number_to_guess = random.randint(lower, upper)
    
    attempts = 0
    guessed = False
    
    # Loop until the user guesses the correct number
    while not guessed:
        # Get user's guess
        try:
            guess = int(input(f"Guess a number between {lower} and {upper}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        except EOFError:
            print("No input received. Exiting the game.")
            return
        
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

# Call the function to start the game
if __name__ == "__main__":
    start_game()

