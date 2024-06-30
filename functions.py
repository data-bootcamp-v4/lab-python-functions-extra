def get_unique_list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list 


def count_case(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return (upper_count, lower_count)

count_case("Hello, World!") # (2, 8)


import string

def remove_punctuation(sentence):
    new_sentence = ""
    for char in sentence:
        if char not in string.punctuation: #string.punctuation is a string containing all punctuation characters in Python
            new_sentence += char
    return new_sentence


def word_count(sentence):
    sentence = remove_punctuation(sentence)
    words = sentence.split()
    return len(words)
