def get_unique_list(lst):
    return list(set(lst))

def count_case(string):
    mayusculas = 0
    minusculas = 0
    
    for char in string:
        if char.isupper():
            mayusculas += 1
        elif char.islower():
            minusculas += 1
            
    return (f"Mayusculas son: {mayusculas}", f"Minusculas son: {minusculas}")

import string

def remove_punctuation(sentence):
    translator = str.maketrans('', '', string.punctuation)
    
    return sentence.translate(translator)

def word_count(sentence):
    punctuation_to_remove = string.punctuation + "¿¡"
    translator = str.maketrans('', '', punctuation_to_remove)
    clean_sentence = sentence.translate(translator)
    words = clean_sentence.split()
    
    return len(words)


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b


def calculate(n1, n2, operador):
    if operador == '+':
        return sumar(n1, n2)
    elif operador == '-':
        return restar(n1, n2)
    elif operador == '*':
        return multiplicar(n1, n2)
    elif operador == '/':
        return dividir(n1, n2)
    else:
        return "Operador no válido"
    


def restar(*args):
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
    return resultado

def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def calculate(operador, *args):
    if not args:
        return "Error: No se proporcionaron números"

    if operador == '+':
        return sumar(*args)
    elif operador == '-':
        return restar(*args)
    elif operador == '*':
        return multiplicar(*args)
    elif operador == '/':
        if len(args) != 2:
            return "Error: La división requiere exactamente dos números"
        return dividir(args[0], args[1])
    else:
        return "Operador no válido"