def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    # your code goes here
    unique_attributes = list(set(lst))
    return unique_attributes

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    # your code goes here
    x = list(string.replace(" ",""))
    up_letters =[]
    lower_letters = []
    for i in x:
        if i.isupper():
            up_letters.append(i)
        elif i.islower():
            lower_letters.append(i)
        else:
            print("Value not a string")
    print("Uppercase count: ", len(up_letters)," , ","Lowercase count: ",len(lower_letters))


def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    # your code goes here
    sent_new = "".join([char for char in sentence if char not in string.punctuation])
    return sent_new

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
    x = remove_punctuation(sentence)
    y = x.strip().split()
    output = len(y)
    print("output:",output)