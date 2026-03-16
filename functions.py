import string

def get_unique_list_f(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


def count_case_f(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower


def remove_punctuation_f(sentence):
    result = ""

    for char in sentence:
        if char not in string.punctuation:
            result += char

    return result


def word_count_f(sentence):
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()
    return len(words)