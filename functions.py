import string

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
    # your code goes here
    uppercase = 0  #initalize uppercase count to 0
    lowercase = 0  #initalize lowercase count to 0
    
    for char in string: # iterate through each character in the string
        if char.isupper(): # check if the character is uppercase
            uppercase +=1 # increment uppercase count
        if char.islower(): # check if the character is lowercase
            lowercase +=1 # increment lowercase count
    return (uppercase , lowercase) # return a tuple with uppercase and lowercase counts

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    for char in sentence: #this will iterate through the sentence
        if char in string.punctuation: # this will check if the char is a punctuation or not
            sentence = sentence.replace(char, "") #this will replace the punctuation with an empty string and replace for a space.
    
    return sentence

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces.
    We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    # your code goes here
    
    words_count = 0
    words = sentence.split(" ") #this use the space as a separator
    for word in words: #this will iterate through the words
        if word != " ":  #this will check if the word is not empty
            words_count += 1 #this will count the words
    return words_count