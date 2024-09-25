def get_unique_list_f(lst):
    lista =[]
    for number  in lst:
        if number not in lista:
            lista.append(number)
    return lista

def count_case_f(string):
    lower=0
    upper=0
    for i in string:
        if i.islower():
            lower+=1                                        
        elif i.isupper():
            upper+=1
    return (upper, lower)

import string

def remove_punctuation_f(sentence):
    text = sentence.translate(str.maketrans("", "", string.punctuation))
    return text 

def word_count_f(frase):
    letras = len(frase.split())
    return letras
