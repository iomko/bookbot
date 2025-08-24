from stats import count_words
from stats import get_book_text
from stats import count_characters
from stats import convert_dic_to_dic_list

import sys

def print_bookbot(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    book_text = get_book_text(file_path)
    print("----------- Word Count ----------")
    words_num = count_words(book_text)
    print(f"Found {words_num} total words")
    print("--------- Character Count -------")
    char_nums = count_characters(book_text)
    char_dic_list = convert_dic_to_dic_list(char_nums)
    for item in char_dic_list:
        key = item["char"]
        val = item["num"]
        if key.isalpha():
            print(f"{key}: {val}")
        pass
    
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]

    print_bookbot(file_path)


if __name__ == "__main__":
    main()
