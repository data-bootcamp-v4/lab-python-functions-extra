def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    # your code goes here
    lst_unique = set(lst)
    return list(lst_unique)

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # your code goes here
    upper = 0
    lower = 0
    for caracter in string:
        if caracter.isupper():
            upper += 1
        else:
            lower += 1
    print(f"Upper case count: {upper}, Lower case count: {lower}")
    return (upper, lower)

def remove_punctuation_f(sentence):
    import string
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    result = ""
    stripped_result = result.strip()
    for character in sentence:
        if character not in string.punctuation:
            stripped_result += character
    return stripped_result

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
    clean = remove_punctuation_f(sentence)
    if not clean:
        return 0
    return len(clean.split())