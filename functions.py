import string


def get_unique_list_f(lst):
    return list(set(lst))


def count_case_f(string_input):
    upper = 0
    lower = 0

    for char in string_input:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower


def remove_punctuation_f(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation))


def word_count_f(sentence):
    cleaned = remove_punctuation_f(sentence)
    words = cleaned.split()
    return len(words)
