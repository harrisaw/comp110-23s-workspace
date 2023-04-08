"""EX06 - CYOA: 2 games of chance: Rock, Paper, Scissors and Coin Toss."""

__author__: str = "730316865"

# Importing function from random.
from random import randint

# Initiating points at 0 and player with empty string.
points: int = 0
player: str = ""

# Setting emoji constants for use in Rock, Paper, Scissors game.
ROCK: str = "\U0001F48E"
PAPER: str = "\U0001F9FB"
SCISSORS: str = "\U0001F52A"

# Setting up dictionaries to assign inputs/random integers to strategies and victory pattern.
choice_dict: dict[int, str] = {1: ROCK, 2: PAPER, 3: SCISSORS}
victory_dict: dict[str, str] = {ROCK: SCISSORS, SCISSORS: PAPER, PAPER: ROCK}

# Setting up emoji constants for use in Coin Toss game.
HEADS: str = "\U0001F600"
TAILS: str = "\U0001F985"

# Setting up dictionary to assign inputs/random integers to strategies.
coin_dict: dict[int, str] = {1: HEADS, 2: TAILS}


# Setting up main game function.
def main() -> None:
    """Main game function."""
    # Calling greeting function.
    greet()

    # Accessing global points variable
    global points

    # Initiating round and game_loop variables.
    round: int = 1
    game_loop: bool = True

    # Starting game loop.
    while game_loop:
        # Updating user on current score and round.
        print(f"Now Starting: Round {round} \nCurrent Score: {points}\n")

        # Looping to have user select a game.
        game_choice = input("Select game choice (enter a number): \n 1: Rock, Paper, Scissors \n 2: Coin Toss \n 3: End Game. \n")
        while game_choice != "1" and game_choice != "2" and game_choice != "3":
            game_choice = input("Select game choice (enter a number): \n 1: Rock, Paper, Scissors \n 2: Coin Toss \n 3: End Game. \n")

        # Calling appropraite function depending on user selection.
        if game_choice == "1":
            rps()
        elif game_choice == "2":
            points = ct(points)
        
        # Ending game loop when prompted by user.
        else:
            print(f"Thanks for playing, {player}! \nYour final score is {points} at Round {round}. \nPlay again soon!")
            game_loop = False

        # Increasing round.
        round += 1


def rps() -> None:
    """Rock, Paper, Scissors game procedure."""
    # Accessing global points and player variables.
    global points, player

    print(f"\nOk, {player}, let's play: Rock, Paper, Scissors!")

    # Prompting user choice of strategy with number input.
    user_choice: str = input(f"Select strategy (enter a number): \n 1: {ROCK} (Rock) \n 2: {PAPER} (Paper) \n 3: {SCISSORS} (Scissors) \n")
    while user_choice != "1" and user_choice != "2" and user_choice != "3":
        user_choice = input(f"Select strategy (enter a number): \n 1: {ROCK} (Rock) \n 2: {PAPER} (Paper) \n 3: {SCISSORS} (Scissors) \n")

    # Converting user strategy to emoji with dictionary.
    user_strategy = choice_dict[int(user_choice)]

    # Using comp_choice function to randomly select opponent strategy.
    comp_strategy = comp_choice()

    # Printing strategies.
    print(f"{player}'s Strategy: {user_strategy}")
    print(f"Opponent Strategy: {comp_strategy}")

    # Printing message and changing score depending on user and generated strategies.
    if user_strategy == comp_strategy:
        print(f"\nYou tied, {player}! Your score does not change.\n")
    # Using victory_dict dictionary to identify user victory.
    elif comp_strategy == victory_dict[user_strategy]:
        print(f"\nCongrats, {player}, you won! Score increases by 1.\n")
        points += 1
    else:
        print(f"\nSorry, {player}, you lost! Score decreases by 1.\n")
        points -= 1


def ct(points: int) -> int:
    """Coin Toss game function."""
    print(f"\nOk, {player}, let's play: Coin Toss")

    # Prompting user choice of strategy with number input.
    user_choice: str = input(f"Select strategy (enter a number): \n 1: {HEADS} (Heads) \n 2: {TAILS} (Tails)\n")
    while user_choice != "1" and user_choice != "2" and user_choice != "3":
        user_choice = input(f"Select strategy (enter a number): \n 1: {HEADS} (Heads) \n 2: {TAILS} (Tails)\n")

    # Converting user strategy to emoji with dictionary.
    user_strategy = coin_dict[int(user_choice)]

    # Using coin_toss function to randomly select correct strategy.
    flip = coin_toss()

    # Printing strategies.
    print(f"{player}'s Choice: {user_strategy}")
    print(f"Correct Choice: {flip}")

    # Printing message and returning changed score depending on result of game.
    if user_strategy == flip:
        print(f"\nCongrats, {player}, you won! Score increases by 1.\n")
        return points + 1
    else:
        print(f"\nSorry, {player}, you lost! Score decreases by 1.\n")
        return points - 1


def greet() -> None:
    """Greeting function."""
    # Greeting the player and providing cotext to the game.
    print("Hello!\nThis adventure allows you to play two games of chance: Rock, Paper, Scissors and Coin Toss!\n")
    print("Each round, you will have the opportunity to increase your score.")
    print("- Winning increases your score by 1. \n- Losses decrease your score by 1. \n- Ties will not affect your score.\n")
    print(f"To win Rock, Paper, Scissors, you must beat a randomly selected strategy. Reminder: \n {ROCK} > {SCISSORS} \n {PAPER} > {ROCK} \n {SCISSORS} > {PAPER}\n")
    print(f"To win Coin Toss, you must match a randomly selected strategy ({HEADS} or {TAILS}).\n")

    # Updating global player variable with user input.
    global player
    player = input("To play, please provide your name: ")
    print(f"Thanks, {player}! Let's begin.\n")


def comp_choice() -> str:
    """Selecting a random oppoenet strategy for Rock, Paper, Scissors."""
    # Selecting randoming integer between 1 and 3.
    random_choice: int = randint(1, 3)

    # Assigning random integer to RPS strategy using dictionary and returning.
    return choice_dict[random_choice]


def coin_toss() -> str:
    """Randomly selecting a correcet strategy for Coin Toss."""
    # Selecting random integer between 1 and 2.
    flip: int = randint(1, 2)
    # Assigning random integer to CT strategy using dictionary and returning.
    return coin_dict[flip]


if __name__ == "__main__":
    main()


# python -m exercises.cyoa
# python -m tools.submission exercises/cyoa.py