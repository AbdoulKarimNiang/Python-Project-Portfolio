import random

number: int = random.choice(range(1, 100 + 1))

print(f"Welcome to the Number Guessing Game! ")
print(f"I'm thinking of a number between 1 and 100.")


def repeat_convert(guess) -> int:
    while not guess.isdigit():
        guess: str = input(f"Make a guess: ")
    guess: int = int(guess)
    return guess


def check_guessing(player_guess) -> bool:
    """ Check for the correctness of the user guess"""
    if player_guess == number:
        print(f"You got it! The answer was {number}.")
        print(f"The game is finished!")
        return True
    elif player_guess > number:
        print(f"Too High.")
        return False
    elif player_guess < number:
        print(f"Too low.")
        return False
    
def reduce_lives(n_lives: int, correct_guess: bool) -> int:
    if correct_guess:
        return n_lives
    else:
        n_lives -= 1
        return n_lives

def game():
    """ This is the Number guessing game"""
    difficulty: str = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    while difficulty not in ['easy', "hard"]:
        difficulty: str = input(f"Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        lives = 10
        for _ in range(1, lives + 1):
            if lives >= 0:
                print(f"You have {lives} attempts to guess the number.")
                player_guess: str = input(f"Make a guess: ")
                guess = repeat_convert(player_guess)
                print(guess)
                correct_guess = check_guessing(guess)
                lives = reduce_lives(lives, correct_guess )
                if correct_guess:
                    print(f"Congratulation you have guessed the correct number: {number} with {lives} lives left")
                    break
            else:
                print(f"You run out of lives. You lost ❌")
    elif difficulty == 'hard':
        lives = 5
        for _ in range(1, lives + 1):
            if lives >= 0:
                print(f"You have {lives} attempts to guess the number.")
                player_guess: str = input(f"Make a guess: ")
                guess = repeat_convert(player_guess)
                print(guess)
                correct_guess = check_guessing(guess)
                lives = reduce_lives(lives, correct_guess )
                if correct_guess:
                    print(f"Congratulation you have guessed the correct number: {number} with {lives} lives left")
                    break
            else:
                print(f"You run out of lives. You lost ❌")
    
    else:
        print(f"You didn't select the correct difficulty. Try again")
game()
