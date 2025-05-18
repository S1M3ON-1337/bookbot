from stats import number_of_words, number_of_character, sorted_character
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = number_of_words(text)
    char_count = number_of_character(text)
    sorted_chars = sorted_character(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    
    print("============= END ===============")

    print(char_count)
    print(f"{num_words} words found in the document")


def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    return file_contents


main()
    