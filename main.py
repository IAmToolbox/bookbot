# BookBot: My first guided project from boot.dev

import sys

from stats import count_words
from stats import count_characters
from stats import sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read() # This method actually reads the file and saves its contents as a string
    return file_contents

def print_report(word_count, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_characters)):
        if sorted_characters[i]["character"].isalpha():
            print(f"{sorted_characters[i]["character"]}: {sorted_characters[i]["count"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = count_words(get_book_text(sys.argv[1]))
    #print(f"{word_count} words found in the document") # I love f-strings
    character_count = count_characters(get_book_text(sys.argv[1]))
    sorted_characters = sort_characters(character_count)
    #print(character_count)
    #print(sorted_characters)
    print_report(word_count, sorted_characters)

main()