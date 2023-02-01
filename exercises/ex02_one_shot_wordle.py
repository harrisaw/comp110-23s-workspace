"""EX02 - One-Shot Wordle."""

__author__: str = "730316865"

# Establishing secret word and finding its length.
secret_word: str = "python"
secret_word_length: int = len(secret_word)

# Establishing user guess word and finding its length.
user_guess = input(f"What is your {secret_word_length}-letter guess? ")
user_guess_length: int = len(user_guess)

# Using while loop to prompt for new guess when guess length not equal secret word length.
while (user_guess_length != secret_word_length):
    user_guess = input(f"That was not {secret_word_length} letters! Try again: ")
    user_guess_length = len(user_guess)

# Setting reference variables different box colors.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

letter_index: int = 0   # Establishing index for loop used below.
output_boxes_basic: str = ""    # Establishing empty string for initial G/W output boxes.

# While loop compares letters of same index in secret word and guess.
# Exact match results in green box, and no match results in white box.
while (letter_index <= (secret_word_length - 1)):
    if (user_guess[letter_index] == secret_word[letter_index]):
        output_boxes_basic = output_boxes_basic + GREEN_BOX
    else:
        output_boxes_basic = output_boxes_basic + WHITE_BOX
    letter_index = letter_index + 1     # Loop control.

letter_index = 0   # Resetting index for use in while loop below.
output_boxes_final: str = ""    # Establishing empty string for final output boxes.

# While loop cycles through each index to construct final output boxes.
while (letter_index <= (secret_word_length - 1)):
    if (output_boxes_basic[letter_index] == GREEN_BOX):
        output_boxes_final = output_boxes_final + GREEN_BOX
        # If the previous loop found an exact match, green box is kept.
    else:
        yellow_check_index: int = 0     # Establishing index for use in while loop to find misplaced letters.
        letter_matches: int = 0     # Establishing counter to track misplaced letters.
        while (yellow_check_index <= (secret_word_length - 1)):
            if (user_guess[letter_index] == secret_word[yellow_check_index]):
                letter_matches = letter_matches + 1
            yellow_check_index = yellow_check_index + 1     # Loop control.
            # Compares unmatched letters in guess to all letters in the secret word.
            # Instances of match are counted, regardless of position in secret word.
        if (letter_matches > 0):
            output_boxes_final = output_boxes_final + YELLOW_BOX
            # Yellow box added to output boxes if letter match is found anywhere in secret word.
        else:
            output_boxes_final = output_boxes_final + WHITE_BOX
            # White box added to output boxes if letter match is not found anywhere in secret word.
    letter_index = letter_index + 1     # Loop control.

print(output_boxes_final)   # Printing finalized output boxes.

# Printing message depending on whether guess matched secret word.
if (user_guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

# python -m exercises.ex02_one_shot_wordle