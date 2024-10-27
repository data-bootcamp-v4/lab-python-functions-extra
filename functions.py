def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    lst = input("Enter a list of numbers separated by a space between each number.").split()
    unique_list = sorted(set(lst))
    return unique_list
    
    print(unique_list)

def count_case_f():
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    string = input("Enter a sentence.")
    uppercase_count = 0
    lowercase_count = 0
    
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count +=1
            
    print(f"Uppercase count: {uppercase_count}, Lowercase count: {lowercase_count}")
    return uppercase_count, lowercase_count

