def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    result = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in result:
            result[lower_char] += 1
        else:
            result[lower_char] = 1
    return result

def sort_on(items):
    return items["num"]

def get_sorted_chars(char_count_dict):
    result = []
    for char in char_count_dict:
        count = char_count_dict[char]
        result.append({"char": char, "num": count})
    result.sort(reverse=True, key=sort_on)
    return result

def print_sorted_chars(sorted_chars):
    for dict in sorted_chars:
        char = dict["char"]
        count = dict["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

