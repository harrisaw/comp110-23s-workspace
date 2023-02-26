"""Ex. 03 Structured Wordle Game."""

__author__: str = "730316865"


def contains_char(target_string: str, search_char: str) -> bool:
    """Returns True if search_char found in target_string."""
    assert len(search_char) == 1       # Requires search_char to be length 1.
    target_len = len(target_string)     # Takes length of word being searched.

    idx = 0     # Setting loop index to 0.
    char_found = False      # Creating output variable default to False.

    # Loops through each character in target string, setting char_found to True if match found.
    while idx < target_len:
        if target_string[idx] == search_char:
            char_found = True
        idx = idx + 1
    # Returning True if search_char found in target string.
    return (char_found)


# Establishing emoji contants.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess_word: str, secret_word: str) -> str:
    """Return emoji string showing character comparison of two strings."""
    assert len(guess_word) == len(secret_word)      # Requires inputs are same length.

    idx = 0     # Setting loop index to 0.
    word_len = len(guess_word)      # Taking word length for while index purposes.
    output_boxes: str = ""      # Creating empty string for output.

    while idx < word_len:
        # Exact character matches at each index add a green box to output string.
        if guess_word[idx] == secret_word[idx]:
            output_boxes = output_boxes + GREEN_BOX
        else:
            # If no exact match, but guess char at index is found in the secret word,
            # yellow box is added to output string. Otherwise, white box added to output string.
            if contains_char(secret_word, guess_word[idx]):
                output_boxes = output_boxes + YELLOW_BOX
            else:
                output_boxes = output_boxes + WHITE_BOX
        idx = idx + 1
    # Return string of output boxes.
    return (output_boxes)


def input_guess(expected_length: int) -> str:
    """Checks input string length is equal to expect length."""
    guess = input(f"Enter a {expected_length} character word: ")        # Takes initial input string.

    # Bool for looping if guess length is not equal to expected length.
    continue_loop = len(guess) != expected_length
    while continue_loop:
        # Update guess.
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
        # Continue loop if new guess length different than expected length.
        continue_loop = len(guess) != expected_length
    # Return guess string of correct length.
    return (guess)


# Establihsing constants for the SECRET_WORD and # of ALLOWED TURNS in game.
# Both can be adjusted as necessary.
SECRET_WORD: str = "codes"
ALLOWED_TURNS: int = 6


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1        # Establishing turn counter used in loop.
    secret = SECRET_WORD        # Setting secret word equal to constant.
    secret_length = len(secret)     # Taking length of secret word for use in input_guess.
    
    while turn < ALLOWED_TURNS + 1:
        print(f"=== Turn {turn}/{ALLOWED_TURNS} ===")       # Print turn statement.
        guess = input_guess(secret_length)      # Use input_guess to take guess of correct length.
        print(emojified(guess, secret))     # Print emoji boxes indicating guess accuracy.
        if guess == secret:     # If correct guess, print victory statement.
            print(f"You won in {turn}/{ALLOWED_TURNS} turns!")
            turn = ALLOWED_TURNS + 1        # Update turns to end the loop.
        else:
            if turn == ALLOWED_TURNS:       # If max turns reached, print loss statement.
                print(f"X/{ALLOWED_TURNS} - Sorry, try again tomorrow!")
            turn = turn + 1     # Update turn to continue loop.


# Allows the game to run as a module.
if __name__ == "__main__":
    main()


# python -m exercises.ex03_wordle
# python -m tools.submission exercises/ex03_wordle.py