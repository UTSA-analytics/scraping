import csv


def write_file(function, description):
    # Opens csv file to append data
    with open('new_function_match.csv', 'a') as csvfile:
        functionwriter = csv.writer(csvfile, delimiter=',')
        data = [function, description]
        # writes data to the file, substitutes "unicode error" for the description if there is a unicode error
        try:
            functionwriter.writerow(data)
        except UnicodeEncodeError:
            data = [function, 'unicode error']
            functionwriter.writerow(data)
        
        csvfile.close()
