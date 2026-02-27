from enum import unique


def get_unique_list(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    list = []
    for i in lst:
        if i not in list:
            list.append(i)
    print(list)


def count_case(string):

    uppercase = 0
    lowercase = 0
    for i in string:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
    print(f"Uppercase count: {uppercase}\nLowercase count: {lowercase}")
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # your code goes here

from itertools import count
from os import remove
import string

from numpy import append


def remove_punctuation(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    new_sentence = []
    for i in sentence:
        if i not in string.punctuation:
            new_sentence.append(i)
    return new_sentence


def word_count(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    no_punct = str.maketrans(" ", " ", string.punctuation)
    sentence = sentence.translate(no_punct).replace("  ", " ")

    count_words = count(len(sentence.split()))
    return count_words
