def get_unique_list_f(lst):
    """
    Takes a list and returns a new list with unique elements.
    """
    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters.
    """
    uppercase_count = 0
    lowercase_count = 0

    for character in string:
        if character.isupper():
            uppercase_count += 1
        elif character.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


def remove_punctuation_f(sentence):
    """
    Removes punctuation marks from a sentence.
    """
    import string
    return sentence.translate(
        str.maketrans("", "", string.punctuation)
    )


def word_count_f(sentence):
    """
    Counts the number of words in a sentence.
    """
    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()

    return len(words)