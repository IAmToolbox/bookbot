# BookBot: My first guided project from boot.dev

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read() # This method actually reads the file and saves its contents as a string
    return file_contents

def count_words(string):
    words = string.split()
    word_count = 0
    for word in words: # Loops once for every word in the input string
        word_count += 1
    return word_count


def main():
    word_count = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{word_count} words found in the document") # I love f-strings

main()