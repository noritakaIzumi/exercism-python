import string


def is_pangram(sentence):
    alphabets = {}
    for char in string.ascii_lowercase:
        alphabets[char] = False

    for char in sentence:
        to_lower = char.lower()
        if to_lower in alphabets.keys():
            alphabets[to_lower] = True

    return not (False in alphabets.values())
