# functions.py

def get_unique_list_f(lst):
    return list(set(lst))

def count_case_f(text):
    mayus = sum(1 for c in text if c.isupper())
    minus = sum(1 for c in text if c.islower())
    return {"Uppercase": mayus, "Lowercase": minus}

def remove_punctuation_f(text):
    import string
    return text.translate(str.maketrans('', '', string.punctuation))

def word_count_f(text):
    return len(text.split())