book_path = "books/frankenstein.txt"

def get_book_path(path):
    # Read the book file at the path given
    with open(path) as f:
        return f.read()

def count_words():
    # Count the number of words from the file
    words = get_book_path(book_path)
    words = words.split()
    return (len(words))

def count_letters():
    # Count the letters from the file
    letters = {}
    book_letters = get_book_path(book_path)
    for letter in book_letters:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sort_by(key):
    # Define what value the list is sorted by
    return key["letter"]

def letter_count_sorted(letter_dictionary):
    # Create a list of letter counts
    letter_list = []
    for letter in letter_dictionary:
        letter_list.append({"letter": letter, "count": letter_dictionary[letter]})
    letter_list.sort(key=sort_by)
    return letter_list

# Print off a report of the data
print(f"====== Report of word count and letters found within {book_path} ======")
print(f"Total words found in the book, {count_words()}\n")

letters_sorted = letter_count_sorted(count_letters())

for letter in letters_sorted:
    if not letter["letter"].isalpha():
        continue
    else:
        print(f"The '{letter['letter']}' letter was found {letter['count']} times")

print("\n====== End of report ======")