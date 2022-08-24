def sum(list):
    result = 0
    for operator in list_operators:
        result += operator
    print(result) 
def subtraction(list):
    result = list_operators[0]
    for i in range (1, (total_operators)):
        result -= list_operators[i]
    print(result) 
def multiplication(list):
    result = list_operators[0]
    for i in range (1, (total_operators)):
        result =  (result * (list_operators[i]))
    print(result) 
def division(list):
    result = list_operators[0]
    for i in range (1, total_operators):
        result = (result / (list_operators[i]))
    print(result) 

next_operation = 1
while (next_operation == 1):
    which_operation = input()
    total_operators = int(input())
    list_operators = []
    for i in range (total_operators):
        operator = int(input())
        list_operators.append(operator)
    if (which_operation == "S"):
        sum(list_operators)
    elif (which_operation == "sub"):
        subtraction(list_operators)
    elif (which_operation == "M"):
        multiplication(list_operators)
    elif (which_operation == "D"):
        division(list_operators)
    next_operation = int(input())
