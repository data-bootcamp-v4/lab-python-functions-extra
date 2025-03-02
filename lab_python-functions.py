def f_get_unique_list(lst):
    return list(set(lst))

def f_count_case(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower

    import string

def f_remove_punctuation(sentence):
    return sentence.translate(str.maketrans("", "", string.punctuation))

def f_word_count(sentence):
    sentence = remove_punctuation(sentence)
    words = sentence.split()
    return len(words)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def calculadora(a, b, operacion):
    if operacion == "suma":
        return suma(a, b)
    elif operacion == "resta":
        return resta(a, b)
    elif operacion == "multiplicacion":
        return multiplicacion(a, b)
    elif operacion == "division":
        return division(a, b)
    else:
        return "Operacion no valida"


def f_calculadora(*args):
    result = args[0]
    for i in range(1, len(args)):
        result = result + args[i]
    return result

