#Sum function
def addition_f(num1, num2):
    result = num1 + num2
    return result

#Subtraction function
def subtraction_f(num1, num2):
    result = num1 - num2
    return result

#Multiplication function 
def multiplicacion_f(num1, num2):
    result = num1 * num2
    return result

#Division function
def division_f(num1, num2):
    if num2 == 0:
        return "Error: division by zero"
    result = num1 / num2
    return result   

#funcion calculator
def calculate_f(arg1, arg2, operator):
    if operator == "+":
        return addition_f(arg1, arg2)
    elif operator == "-":
        return subtraction_f(arg1, arg2)
    elif operator == "*":
        return multiplicacion_f(arg1, arg2) 
    elif operator == "/":
        if arg2 == 0:
            print("The second argument is 0, try again with another number.")
            return None
        else:
            return division_f(arg1, arg2)
    else: 
        print("Invalid Operator")