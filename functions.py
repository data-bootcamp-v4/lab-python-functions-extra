def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    # your code goes here
    
    unique_numbers = []
    
    for number in lst:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers

lst = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = get_unique_list_f(lst)
print(unique_numbers)

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # your code goes here
    count_upper = 0
    count_lower = 0
    for char in string:
        if char.isupper():
            count_upper += 1
        elif char.islower():
                count_lower += 1
    return count_upper, count_lower

string = "Hello World!"
count_upper, count_lower = count_case_f(string)
print(f"Uppercase letters: {count_upper}, Lowercase letters: {count_lower}")

import string

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here

    replaced = sentence.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    return replaced


def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    # your code goes here
    
    replaced = sentence.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    length = len(replaced.split())
    return length

sentence = "Hello, is this an example sentence? Yes, it is!"
replaced = remove_punctuation_f(sentence)
print (replaced)

sentence = "Hello, is this an example sentence? Yes, it is!"
length = word_count_f(sentence)
print (length)