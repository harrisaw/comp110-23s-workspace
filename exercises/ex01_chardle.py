"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730316865"

# Getting user inputs and returning errors when neccessary.
input_word = input("Enter a 5-character word: ")

if (len(input_word) != 5):
    print("Error: Word must contain 5 characters.")
    exit()

search_letter = input("Enter a single character: ")

if (len(search_letter) != 1):
    print("Error: Character must be a single character.")
    exit()

# Initiating search and match counter
print("Searching for " + search_letter + " in " + input_word)

match_count: int = 0

# Checking for match at index 0, counting if match occurs.
if (input_word[0] == search_letter):
    print(search_letter + " found at index 0")
    match_count = match_count + 1

# Checking for match at index 1, counting if match occurs.
if (input_word[1] == search_letter):
    print(search_letter + " found at index 1")
    match_count = match_count + 1

# Checking for match at index 2, counting if match occurs.
if (input_word[2] == search_letter):
    print(search_letter + " found at index 2")
    match_count = match_count + 1

# Checking for match at index 3, counting if match occurs.
if (input_word[3] == search_letter):
    print(search_letter + " found at index 3")
    match_count = match_count + 1

# Checking for match at index 4, counting if match occurs.
if (input_word[4] == search_letter):
    print(search_letter + " found at index 4")
    match_count = match_count + 1

# Printing results of search, wording dependent on count total.
if (match_count > 0):
    if (match_count > 1):
        print(str(match_count) + " instances of " + search_letter + " found in " + input_word)
    else:
        print("1 instance of " + search_letter + " found in " + input_word)
else:
    print("No instances of " + search_letter + " found in " + input_word)
