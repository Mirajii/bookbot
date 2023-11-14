def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document \n")
    for i in get_letters(text):
        print(f"The '{i[0]}' character was found {i[1]} times")


 #   print(get_letters(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(text.split())

def get_letters(text):
    characters={}
    letters = []
    for character in text.lower():
        if character.isalpha():
            if character not in characters.keys():
                characters[character] = 1
            else:
                characters[character] += 1
    letters = list(characters.items())
    return sorted(letters)
main()