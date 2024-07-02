def get_unique_list_f(lst):
    return list(set(lst))

def count_case_f(string):
    lower_count = 0
    upper_count = 0
    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    return upper_count, lower_count

def remove_punctuation_f(sentence):
    sentence = sentence.replace('.','')
    sentence = sentence.replace(',','')
    sentence = sentence.replace('!','')
    sentence = sentence.replace('?','')
    sentence = sentence.replace('¡','')
    sentence = sentence.replace('¿','')
    sentence = sentence.replace(':','')
    sentence = sentence.replace(')','')
    return sentence

def word_count_f(sentence):
    count_words = 0
    sentence = remove_punctuation_f(sentence)
    sentence_splited = sentence.split()
    for word in sentence_splited:
        if word != ' ':
            count_words += 1
    return count_words