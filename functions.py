# In functions.py
def get_unique_list_f(lst):
    return list(set(lst))

def count_case_f(string):
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    return upper_count, lower_count

import string
def remove_punctuation_f(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation))

def word_count_f(sentence):
    cleaned_sentence = remove_punctuation_f(sentence)
    return len(cleaned_sentence.split())
