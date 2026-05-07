import string as str_module

def get_unique_list_f(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def count_case_f(string_input):
    uppercase_count = 0
    lowercase_count = 0
    for char in string_input:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return uppercase_count, lowercase_count

def remove_punctuation_f(sentence):
    clean_sentence = ""
    for char in sentence:
        if char not in str_module.punctuation:
            clean_sentence += char
    return clean_sentence

def word_count_f(sentence):
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()
    return len(words)


print(get_unique_list_f([1, 2, 3, 3, 3, 4, 5]))               # [1, 2, 3, 4, 5]
print(count_case_f("Hello World"))                             # (2, 8)
print(remove_punctuation_f("Hello, World!!!"))                 # Hello World
print(word_count_f("Note : this is an example !!! Good day :)"))  # 7