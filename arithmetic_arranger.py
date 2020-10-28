def arithmetic_arranger(problems):
    print(problems)
    if len(problems) > 4:
        return "Error: Too many problems."
    
    for problem in problems:
        num1, operator, num2 = problem.split()
        #print(num1, operator, num2)
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if num1.isdecimal() == False or num2.isdecimal() == False:
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        

    return