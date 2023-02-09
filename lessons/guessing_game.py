"""Ask for number, give hints about number if wrong"""

SECRET: int = 10    # Caps since it shouldn't change.
guess: int = int(input("Guess a number! "))
playing: bool = True

while playing:
    if guess == SECRET:
        print("Correct! You did it!")
        playing = False
    else:
        if guess < SECRET:
            guess = int(input("Wrong! Secret number is higher. Guess again!"))
        else:
            guess = int(input("Wrong! Secret number is lower. Guess again!"))

