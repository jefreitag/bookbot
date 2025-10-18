def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
    return file_contents

def find_word_num(text):
    return len(text.split())

def main():
    word_num = find_word_num(get_book_text('./books/frankenstein.txt'))
    print(f"Found {word_num} total words")

main()