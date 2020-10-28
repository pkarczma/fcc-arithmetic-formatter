def arithmetic_arranger(problems, addanswers = False):
    # Return if number of problems is more than 5
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Create an empty array of arrays, where
    # each element keeps the contents for each line
    arrline = [[],[],[],[]]
    # For each problem
    for problem in problems:
        # Extract values and an operator
        value1, operator, value2 = problem.split()
        # Operator must be either '+' or '-'
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        # Values must be decimal
        if value1.isdecimal() == False or value2.isdecimal() == False:
            return "Error: Numbers must only contain digits."
        # Values must consist of maximum 4 digits
        if len(value1) > 4 or len(value2) > 4:
            return "Error: Numbers cannot be more than four digits."
        maxlen = max(len(value1), len(value2))
        arrline[0].append(value1.rjust(maxlen + 2))
        arrline[1].append(operator + value2.rjust(maxlen + 1))
        arrline[2].append("".rjust(maxlen + 2, "-"))
        if operator == "+":
            arrline[3].append(str(int(value1) + int(value2)).rjust(maxlen + 2))
        else:
            arrline[3].append(str(int(value1) - int(value2)).rjust(maxlen + 2))

    arranged = ""
    lines = len(arrline) - int(addanswers == False)
    for ii in range(lines):
        for jj in range(len(problems)):
            arranged = arranged + str(arrline[ii][jj]) + "    "
        arranged = arranged.rstrip()
        if ii < lines - 1:
            arranged += "\n"
    arranged.rstrip()
    
    return arranged