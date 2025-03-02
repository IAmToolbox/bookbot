# BookBot: My first guided project from boot.dev

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read() # This method actually reads the file and saves its contents as a string
    return file_contents

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()