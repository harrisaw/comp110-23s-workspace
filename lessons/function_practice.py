"""Function Practice"""

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return(my_words)

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if (letter_idx < len(my_words)-1):
        return(my_words[letter_idx])
    else:
        return("Too high of an index")

test_word: int = "Python!"
response: str = mimic_letter(test_word, 0)
# print(response)

idx: int = 0
while idx < len(test_word)-1:
    print(mimic_letter(test_word, idx))
    idx = idx + 1
