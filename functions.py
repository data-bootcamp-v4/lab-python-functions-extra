import string

def get_unique_list_f(lst):
    return list(set(lst))

def count_case_f(string_):
    upper_count = sum(1 for c in string_ if c.isupper())
    lower_count = sum(1 for c in string_ if c.islower())
    return (upper_count, lower_count)

def remove_punctuation_f(sentence):
    translator = str.maketrans('', '', string.punctuation)
    return sentence.translate(translator)

def word_count_f(sentence):
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()
    return len(words)