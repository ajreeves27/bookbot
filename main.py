import sys
from stats import get_num_words, get_char_nums, chars_to_sorted_list


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")

    num_words = get_num_words(filepath)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    letter_counts = get_char_nums(filepath)
    sorted_chars = chars_to_sorted_list(letter_counts)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()