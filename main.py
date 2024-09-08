def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    words_num = word_count(text)
    char_num = char_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_num} words found in the document")
    print_report_char(char_num)
    print("--- End report ---")


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

def print_report_char(dict):
    chars = []
    for key,value in dict.items():
        if key.isalpha():
            new_dict = {}
            new_dict[key] = value
            chars.append(new_dict)
    
    bubble_sort(chars)

    for i in chars:
        key = list(i.keys())[0]  # Extract the first (and only) key
        value = list(i.values())[0]  # Extract the first (and only) value
        print(f"The '{key}' character was found {value} times")

    
def bubble_sort(chars):
    n = len(chars)
    # Outer loop to go through the list multiple times
    for i in range(n):
        # Inner loop to compare adjacent elements
        for j in range(0, n-i-1):
            # Access the values of the current dictionary and the next one
            current_value = list(chars[j].values())[0]
            next_value = list(chars[j+1].values())[0]
            
            # If current value is less than the next, swap them (for descending order)
            if current_value < next_value:
                chars[j], chars[j+1] = chars[j+1], chars[j]
        


if __name__ == "__main__":
    main()

