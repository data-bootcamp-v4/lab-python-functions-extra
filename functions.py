def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    lista_unicos = []
    for objeto in lst:
        if objeto in lista_unicos:
            pass
        else:
            lista_unicos.append(objeto)
    return lista_unicos
    # your code goes here


def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # your code goes here
    cuenta = ({"mayuscula": 0}, {"miniscula": 0})
    for letra in string:
        
        if letra == " ":
            pass
            
        elif letra == str(letra).upper():
            cuenta[0]["mayuscula"] += 1
            
        else:
            cuenta[1]["miniscula"] += 1
        
    return cuenta
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
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    return sentence


def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    palabras = sentence.split()
    return f"el numero de palabras es : {len(palabras)}"

