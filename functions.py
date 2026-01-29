def get_unique_list_f(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


numbers = [1, 2, 3, 3, 3, 3, 4, 5]

result = get_unique_list_f(numbers)

print(result)
print(type(result))


def count_case_f(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1 #upper_count = upper_count + 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

text = "Hello World!"
result = count_case_f(text)
print(result)


import string

def remove_punctuation_f(sentence):
    result = " "
    for char in sentence:
        if char not in string.punctuation:
            result += char

    return result      

text = "Note : this is an example !!! Good day : )"
clean_text = remove_punctuation_f(text)
print(clean_text)



def word_count_f(sentence):
    words = sentence.split()
  
    return len(words)

words_number = word_count_f(clean_text)
print(words_number)
