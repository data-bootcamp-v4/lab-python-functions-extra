import string


def get_unique_list_f(lst):
    new_list = set(lst)
    new_list = list(new_list)
    return new_list


def count_case_f(string):
    uppercase_count = 0
    lowercase_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_count += 1
        elif letter.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


def remove_punctuation_f(sentence):
    new_sentence = str()

    for character in sentence:
        if character not in string.punctuation:
            new_sentence += character

    return new_sentence


def word_count_f(sentence):
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()
    contar = len(words)
    return contar