def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    puntuacion = ".,!?):"
    result = ""

    for char in sentence:
        if char not in puntuacion:
            result += char
    return result

sentence = "Note : this is an example !!! Good day : )"

final_sentence = remove_punctuation_f(sentence)
print(final_sentence)


def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    cleaned = remove_punctuation_f(sentence)
    words = cleaned.split() # Divide por espacios
    return len(words)

count_words = word_count_f(sentence)
print(f'El numero de palabras son: {count_words}')