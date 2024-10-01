import string

def get_unique_list_f(lst):
    unique_elements = list(set(lst))
    return unique_elements

def count_case_f(string):
    uppercase_count = 0
    lowercase_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return (uppercase_count, lowercase_count)

def remove_punctuation_f(sentence):
    return "".join(char for char in sentence if char not in string.punctuation)


def word_count_f(sentence):
    cleaned_sentence = remove_punctuation_f(sentence)
    words = cleaned_sentence.split()
    return len(words)