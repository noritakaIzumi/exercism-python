"""Little Sister's Essay

https://exercism.org/tracks/python/exercises/little-sisters-essay

"""


def capitalize_title(title: str) -> str:
    """

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    """

    def capitalize_str(word_: str) -> str:
        return word_.capitalize()

    return ' '.join(map(capitalize_str, title.split()))


def check_sentence_ending(sentence: str) -> bool:
    """

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """

    return sentence[-1] == '.'


def clean_up_spacing(sentence: str) -> str:
    """

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    """

    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """

    :param sentence: str a sentence to replace words in.
    :param old_word: str word to replace
    :param new_word: str replacement word
    :return:  str input sentence with new words in place of old words
    """

    return sentence.replace(old_word, new_word)
