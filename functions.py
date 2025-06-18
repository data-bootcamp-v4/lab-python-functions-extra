def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    result = []
    
    for word in lst:
        if result.count(word) == 0:
            result.append(word)
    
    return result

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    uppercase = 0
    lowercase = 0
    for letter in string:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1

    print ('Uppercase count:', uppercase, 'lowercase count:', lowercase)

    return


def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    result =''
    for letter in sentence:
        if letter.isalpha() or letter.isspace():
            result+= letter
    
    return (result)

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """

    words = remove_punctuation_f(sentence).split()
    return(len(words))

def addition_f (x,y):
    addition = x+y
    return addition

def multiplication_f (x,y):
    multiplication = x*y
    return multiplication

def substraction_f (x,y):
    substraction = x-y
    return substraction

def division_f (x,y):
    try:
        division  = x/y
    except ZeroDivisionError:
        print ('Zero division error. Try something else.')
        return None
    return division 

def calculate_f (x,y, operator):
    if operator == addition_f:
        print (addition_f (x,y))
    elif operator == multiplication_f:
        print (multiplication_f (x,y))
    elif operator == substraction_f:
        print (substraction_f (x,y))
    elif operator == division_f:
        print (division_f(x,y))

    return



