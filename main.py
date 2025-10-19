from stats import get_num_words, get_char_counts

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
    return file_contents

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    word_num = get_num_words(book_text)
    print(f"Found {word_num} total words")
    print(get_char_counts(book_text))
    

main()