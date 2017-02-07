def check_string(function):
    # Finds functions that end in A or W and strips the A or W from the end
    length = (len(function)-1)
    if function[length] == ('A'):
        function1 = function[:-1]
    elif function[length] == ('W'):
        function1 = function[:-1]
    else:
        function1 = function
    return(function1)
