# Functions that analyze the text

def count_words(string):
    words = string.split()
    word_count = 0
    for word in words: # Loops once for every word in the input string
        word_count += 1
    return word_count

def count_characters(string):
    character_dict = {} # Initialize the character dictionary
    for character in string:
        character = character.lower() # Turn characters into lowercase to avoid duplicates
        if character in character_dict: # Catch any characters that may not be in the dictionary yet
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict
