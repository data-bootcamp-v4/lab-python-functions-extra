import string
import re


def addition_f(lst):
    return sum(lst)

def subtraction_f(lst):
    if len(lst) == 0: 
        return
    return lst[0] - sum(lst[1:])

def multiplication_f(lst):
    result = 1
    for x in lst:
        result *= x
    return result

def division_f(lst):
    if len(lst) == 0: 
        return
    result = lst[0]
    for x in lst[1:]:
        result /= x
    return result

def calculate_f(**kwargs):
    """
    input = calculate_opt("-"=[1,2,3,4,5])
    returns 1-2-3-4-5

    input = calculate_opt("+"=[1,2,3,4,5])
    returns 1#

    """
    results = []
    for operator, value in kwargs.items():
        if operator == "plus":
            results.append(addition_f(value))
        elif operator == "minus":
            results.append(subtraction_f(value))
        elif operator == "mult": 
            results.append(multiplication_f(value))
        elif operator == "div":
            results.append(division_f(value))
        else: 
            print("Wrong operator!")
    return results

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
    return (sum(x.isupper() for x in string), sum(x.islower() for x in string))


def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    pattern = r"\w+|[^\s\w^[']]+"
    return " ".join(re.findall(pattern, sentence))

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    return len(remove_punctuation_f(sentence).split(" "))
