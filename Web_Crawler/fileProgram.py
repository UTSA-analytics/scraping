import csv

# Opens statically assigned folder, reads folder and returns an array of functions
def get_file_input():
    fr = open('Functions.csv', 'r')
    text = fr.read()
    functions = text.split()
    fr.close()
    return functions

    
