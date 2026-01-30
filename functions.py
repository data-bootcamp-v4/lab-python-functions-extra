lst = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]

def get_unique_list_f(lst):
    list = []
    for number in lst:
        if number not in list:
            list.append(number)
            return list

get_unique_list_f(lst)

string = "Hello Ironhack"

def count_case_f(string):
    upper_count = 0
    lower_count = 0 
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

count_case_f(string)

import string
sentence = "Some say, life is but a dream, Some say it's a test?"
def remove_punctuation_f(sentence):
    return sentence.translate(str.maketrans('', '' , string.punctuation))

remove_punctuation_f(sentence)