import string

def get_unique_list_f(lst):
    new = set()
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    for x in lst :
        if x in new :
            pass
        else : 
            new.add(x)
    
    # your code goes here

    return list(new)

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    liste_exemple = (list(string))
    maj =[]
    minu =[]
    for x in liste_exemple: 
        if x == x.upper() and x != ' ':
            maj.append(x)
        elif  x == x.lower() and x != ' ':
            minu.append(x)
        else :
            pass
    return (f'majuscules : {len(maj)} , minuscules {len(minu)}, ')

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    new_phrase = sentence.translate(str.maketrans('','', string.punctuation))
    return new_phrase

def word_count_f(new_phrase):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    phrase2 = list(new_phrase.split())
    return (len(phrase2))