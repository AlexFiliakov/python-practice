def is_pangram(sentence):
    """Determine if a sentence is a pangram.
    (a pangram uses every letter of the alphabet.)

    Arguments:
    sentence -- text string
    """
    track_letters = {} # Track which letters get found

    for char in sentence.lower():
        if char.isalpha():
            track_letters[char] = True

    LETTERS_IN_ALPHABET = 26
    return len(track_letters) == LETTERS_IN_ALPHABET


# Alternate solution:
from string import ascii_lowercase
ALPHABET = set(ascii_lowercase)
def is_pangram_terse(string):
    return ALPHABET.issubset(string.lower())
