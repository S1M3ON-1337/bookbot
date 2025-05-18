def number_of_words(text):
    list_of_words = text.split()
    num_words = len(list_of_words)
    return num_words
    
def number_of_character(text):
    char_count = {}
    text = text.lower()

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    
    return char_count


def sorted_character(char_count):
    char_list = []

    for char, count in char_count.items():
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)

    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

    