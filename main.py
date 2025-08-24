from stats import count_words
from stats import get_book_text
from stats import count_characters

def main():
    book_text = get_book_text("books/frankenstein.txt")
    char_nums = count_characters(book_text)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    print(char_nums)

if __name__ == "__main__":
    main()
