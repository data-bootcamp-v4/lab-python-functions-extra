
import string

def get_unique_list_f(lst):
    list_uniq = []
    for number in lst:
        if number not in list_uniq:
            list_uniq.append(number)
    return list_uniq


def count_case_f(string):

    upper_count = 0
    lower_count = 0
   
    for letter in string:
        if letter.isupper():
            upper_count +=1
        elif letter.islower():
            lower_count +=1
            
    return (upper_count,lower_count)


def remove_punctuation_f(sentence):
   
    clean_sentence = ""
    for char in sentence:
        if char not in string.punctuation:
            clean_sentence += char
    return(clean_sentence)



def word_count_f(sentence):

    clean_sentence = remove_punctuation_f(sentence)
    words = clean_sentence.split()
    words_number = len(words)

    return words_number