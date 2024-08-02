def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text.lower())
    char_count = get_chars_dict(text)
    

    #print(char_count)

    print("--- Begin book report on Frankenstein ---")
    print(f"{num_words} words found in the document")
    char_keys = list(char_count.keys())
    char_values = list (char_count.values())
    for i in range(len(char_keys)):
        print(f"The character '{char_keys[i]}' was found {char_values[i]} times.")
    print("--- End Report ---")





def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    char_keys = list(chars.keys())
    char_keys.sort()
    sorted_chars = {i:chars[i] for i in char_keys}
    
    
    return sorted_chars      

main()
