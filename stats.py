# Functions that analyze the text

def count_words(string):
    words = string.split()
    word_count = 0
    for word in words: # Loops once for every word in the input string
        word_count += 1
    return word_count