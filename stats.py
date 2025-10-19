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