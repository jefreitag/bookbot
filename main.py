from stats import get_num_words, get_char_counts, get_sorted_chars, print_sorted_chars
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
    return file_contents

def main():
    args = sys.argv
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_location = sys.argv[1]
    book_text = get_book_text(f'./{book_location}')
    word_num = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")
    print_sorted_chars(get_sorted_chars(get_char_counts(book_text)))

    

main()