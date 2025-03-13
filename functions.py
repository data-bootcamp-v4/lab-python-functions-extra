import string

def get_unique_list_f(lst):
    """Returns a list of unique elements from the given list."""
    return list(set(lst))

def count_case_f(string):
    """Returns the count of uppercase and lowercase letters in a string."""
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())
    return uppercase_count, lowercase_count

def remove_punctuation_f(sentence):
    """Removes punctuation from the given sentence."""
    return "".join(char for char in sentence if char not in string.punctuation)

def word_count_f(sentence):
    """Counts the number of words in a sentence after removing punctuation."""
    cleaned_sentence = remove_punctuation_f(sentence)
    words = cleaned_sentence.split()
    return len(words)
