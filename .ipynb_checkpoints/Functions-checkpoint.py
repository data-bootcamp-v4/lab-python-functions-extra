def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    return list(set(lst))

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    count_upper = 0
    count_lower = 0
    
    for char in string:
        if char.isupper():
            count_upper += 1
        else:
            count_lower += 1
    return print(f"Uppercase count: {count_upper}, Lowercase count: {count_lower}")

import string
import re

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    return re.sub(r'[^\w\s]', '', sentence)
    
def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    return len(remove_punctuation_f(sentence).split())

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def calculate_f(operator, x, y):
    if operator == '+':
        return addition(x,y)
    elif operator == '-':
        return subtraction(x,y)
    elif operator == '*':
        return multiplication(x,y)
    elif operator == '/':
        return division(x,y)
    else:
        return "Invalid operator."