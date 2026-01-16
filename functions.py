def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    # your code goes here
    new_list = list(set(lst))
    return new_list

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # your code goes here
    up = 0
    low = 0
    for char in string:
            if char.isupper():
                up += 1
            elif char.islower():
                low += 1
    t = (up, low)
    print(f"Uppercase count: {up}, Lowercase count: {low}")
    return t


def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    new_string = sentence.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(':', '')
    print(new_string)
    return new_string

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
    cleaned_sentence = remove_punctuation_f(sentence)
    words = cleaned_sentence.split()
    count = len(words)
    print(f"Word count: {count}")
    return count


