def get_unique_list_f(lst):
    
    lst = list(set(lst))
    return lst

def count_case_f(string):
    
    count_upper = 0
    count_lower = 0

    for letter in string:
        if letter.isupper():
            count_upper += 1
        elif letter.islower():
            count_lower += 1
    return (count_upper, count_lower,)

import string

def remove_punctuation_f(sentence):

    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    return sentence

def word_count_f(sentence):

    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    sentence = sentence.strip()
    words = sentence.split()
    return len(words)
    