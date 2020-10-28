def arithmetic_arranger(problems, addanswers = False):
    # Return if number of problems is more than 5
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Create an empty array of strings per each line
    line = ["", "", "", ""]
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
        # Extract maximum length of values
        maxlen = max(len(value1), len(value2))
        # Append justified elements and spaces to each line
        line[0] += value1.rjust(maxlen + 2) + "    "
        line[1] += operator + value2.rjust(maxlen + 1) + "    "
        line[2] += (maxlen + 2) * '-' + "    "
        if operator == "+":
            line[3] += str(int(value1) + int(value2)).rjust(maxlen + 2) + "    "
        else:
            line[3] += str(int(value1) - int(value2)).rjust(maxlen + 2) + "    "

    # Create an arranged string
    arranged = line[0].rstrip() + '\n' + line[1].rstrip() + '\n' + line[2].rstrip()
    # Add answers to the arranged string
    if addanswers == True:
        arranged += '\n' + line[3].rstrip()
    
    # Return arranged string
    return arranged