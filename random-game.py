import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Number Guessing Game!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {target_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")


number_guessing_game()