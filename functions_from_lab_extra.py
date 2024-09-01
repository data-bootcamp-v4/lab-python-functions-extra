def get_unique_list_f(lst):

    temporal_set = set(lst)
    new_list = list(temporal_set)
    return new_list


def count_case_f(string):

    lower_count = 0
    upper_count = 0
    for x in string:
        if x.isupper():
            upper_count += 1
        elif x.islower():
            lower_count += 1
    
    return [lower_count, upper_count]


def remove_punctuation_f(sentence):

    return sentence.replace(",", "").replace("!","").replace("?", "").replace(": ", "").replace("  ", " ").replace(")", "")


def word_count_f(sentence):

    no_punctuation_sentence = remove_punctuation_f(sentence).strip()
    word_list = []
    for x in no_punctuation_sentence.split(" "):
        word_list.append(x)

    return len(word_list)