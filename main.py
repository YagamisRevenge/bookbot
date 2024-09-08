def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    words_num = word_count(text)
    char_num = char_count(text)
    print(f"There are {words_num} words in this book!")


def char_count(str):
    new_str = str.lower()
    count = {}
    for i in range(len(new_str)):
        if new_str[i] in count:
            count[new_str[i]] += 1
        else:
            count[new_str[i]] = 1
    return(count)


def book_text(path):
    with open(path) as f:
        return f.read()

def word_count(str):
    words = str.split(" ")
    return len(words)

if __name__ == "__main__":
    main()

