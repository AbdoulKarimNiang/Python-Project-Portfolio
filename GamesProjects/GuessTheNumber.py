import random

number: int = random.choice(range(1, 100 + 1))

print(f"Welcome to the Number Guessing Game! ")
print(f"I'm thinking of a number between 1 and 100.")


def repeat_convert(guess) -> int:
    while not guess.isdigit():
        guess: str = input(f"Make a guess: ")
    guess: int = int(guess)
    return guess


def check_guessing(player_guess) -> None:
    """ Check for the correctness of the user guess"""
    if player_guess == number:
        print(f"You got it! The answer was {number}.")
        print(f"The game is finished!")
    elif player_guess > number:
        print(f"Too High.")
        print(f"Guess again.")
    elif player_guess < number:
        print(f"Too low.")
        print(f"Guess again.")


def game():
    """ This is the Number guessing game"""
    difficulty: str = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    while difficulty not in ['easy', "hard"]:
        difficulty: str = input(f"Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        lives = 10
        print(f"You have {lives} attempts to guess the number.")
        player_guess: str = input(f"Make a guess: ")
        guess = repeat_convert(player_guess)
        print(guess)
        for _ in range(1, lives + 1):
            check_guessing(guess)
            player_guess: str = input(f"Make a guess: ")
            guess = repeat_convert(player_guess)
    elif difficulty == 'hard':
        lives = 5
        print(f"You have {lives} attempts to guess the number.")
        player_guess: str = input(f"Make a guess: ")
        guess = repeat_convert(player_guess)
        print(guess)
        for _ in range(1, lives + 1):
            check_guessing(guess)
            player_guess: str = input(f"Make a guess: ")
            repeat_convert(player_guess)
            if player_guess != number:
                lives -= 1
                print(f"You have {lives} attempts to guess the number.")
            if player_guess == number:
                break
            player_guess: int = int(input(f"Make a guess: "))
    else:
        print(f"You didn't select the correct difficulty. Try again")
game()
