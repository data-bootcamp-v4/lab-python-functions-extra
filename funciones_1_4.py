
def f_remove_punctuation(sentence):

    sentence = sentence.replace('.', '')
    sentence = sentence.replace(',', '')
    sentence = sentence.replace('!', '')
    sentence = sentence.replace('?', '')
    sentence = sentence.replace(':', '')
    sentence = sentence.replace(';', '')
    sentence = sentence.replace(')', '')
    
    return sentence

def f_word_count(sentence):

    sentence_no_punctuation = f_remove_punctuation(sentence)
    
    # Luego, contamos las palabras separándolas por espacios
    words = sentence_no_punctuation.split()
    
    return len(words)

def f_count_case(string):

    mayusc_count = 0
    minusc_count = 0

    for char in string:
        if char.isupper():  # Verifica si el carácter es mayúscula
            mayusc_count += 1
        elif char.islower():  # Verifica si el carácter es minúscula
            minusc_count += 1
    
    return print(f'Uppercase count: {mayusc_count}, Lowercase count: {minusc_count}')

def f_get_unique_list(lst):

    return list(set(lst))