#Sum function
def get_unique_list_f(num1, num2):
    result = num1 + num2
    return result

#Subtraction function
def count_case_f(num1, num2):
    result = num1 - num2
    return result

#Multiplication function 
def remove_punctuation_f(num1, num2):
    result = num1 * num2
    return result

#Division function
def word_count_f(num1, num2):
    if num2 == 0:
        return "Error: division by zero"
    result = num1 / num2
    return result   

#funcion calculator
def calculate_f(arg1, arg2, operator):
    if operator == "+":
        return get_unique_list_f(arg1, arg2)
    elif operator == "-":
        return count_case_f(arg1, arg2)
    elif operator == "*":
        return remove_punctuation_f(arg1, arg2) 
    elif operator == "/":
        if arg2 == 0:
            print("The second argument is 0, try again with another number.")
            return None
        else:
            return word_count_f(arg1, arg2)
    else: 
        print("Invalid Operator")