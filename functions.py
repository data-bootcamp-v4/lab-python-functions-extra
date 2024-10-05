# functions.py

def get_unique_list_f(input_list):
    """Return a list of unique elements from the input list."""
    return list(set(input_list))

def count_case_f(s):
    """Count the number of uppercase and lowercase letters in a string."""
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

def remove_punctuation_f(s):
    """Remove punctuation from the input string."""
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

def word_count_f(s):
    """Count the number of words in the input string."""
    return len(s.split())
