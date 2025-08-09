import sys
from stats import count_words, count_chars, sort_dict

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    book_text = get_book_text(file_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    
    chars_dict = count_chars(book_text)

    sorted_chars = sort_dict(chars_dict)
    
    for t in sorted_chars:
        print(f'{t["char"]}: {t["num"]}')

main()