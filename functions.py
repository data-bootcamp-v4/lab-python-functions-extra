def get_unique_list_f(lst):
    return list(set(lst))

def count_case_f(string):
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return f"Uppercase count: {uppercase_count}, Lowercase count: {lowercase_count}"

def remove_punctuation_f(sentence):
    import string
    no_punctuation = ''.join([char for char in sentence if char not in string.punctuation])
    return no_punctuation

def word_count_f(sentence):
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()
    return len(words)