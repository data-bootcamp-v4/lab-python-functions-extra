import string


def get_unique_list_f(lst):
    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


def count_case_f(string_value):
    uppercase_count = 0
    lowercase_count = 0

    for character in string_value:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1

    return (uppercase_count, lowercase_count)


def remove_punctuation_f(sentence):
    clean_sentence = ""

    for character in sentence:
        if character not in string.punctuation:
            clean_sentence += character

    return clean_sentence


def word_count_f(sentence):
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()

    return len(words)

    from functions import (
    get_unique_list_f,
    count_case_f,
    remove_punctuation_f,
    word_count_f
)def remove_punctuation_f(sentence):
    clean_sentence = ""

    for character in sentence:
        if character not in string.punctuation:
            clean_sentence += character

    return clean_sentence


def word_count_f(sentence):
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()

    return len(words)


    def remove_punctuation_f(sentence):
    clean_sentence = ""

    for character in sentence:
        if character not in string.punctuation:
            clean_sentence += character

    return clean_sentence


def word_count_f(sentence):
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()

    return len(words)