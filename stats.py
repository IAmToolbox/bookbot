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

# Time to figure out how to sort this bullshit

def sort_on(dict): # Function to get a proper sorted list
    return dict["count"]

def sort_characters(character_dict):
    sorted_list = [] # Initialize empty list for sorting
    for character in character_dict:
        sorted_list.append({"character": character, "count": character_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    