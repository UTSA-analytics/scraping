import requests
from bs4 import BeautifulSoup
import re
import fileProgram
import find_description
import write_file
import function_test
import sys
import time

def match_functions():
    # intiates final result, sets as global variable
    final_result = 'None'
    # gets contents of file and iterates through each function in the file 
    functions = fileProgram.get_file_input()
    for function in functions:
        # Sleep function used conserve resources and to avoid being blocked
        time.sleep(1)
        # This line strips W or A off of the function name when searching
        original_function = function
        function = function_test.check_string(function)
        # initiates result string to be used later
        result_string = []
        # search for the function on yahoo.com 
        url = ((r"https://search.yahoo.com/search?p=" + function +
               "&ei=UTF-8&fp=1&nojs=1"))
        # Retrieve the page source code and iterate through the anchors to find the href links saves the links in an array
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.find_all('a', href=True):
            result = link.get('href')
            result_string.append(result)
            # exits program if security warning pops up
            if result_string[0] == r"u'http://us.rd.yahoo.com/500/*http://www.yahoo.com'":
                sys.exit()  
        #This is for monitoring purposes, prints the 18th link in the array to ensure        
        print(result_string[18])
        result_string = str(result_string)
        result_string = result_string.split()
        # iterates through the links and breaks once it finds the msdn link
        for result in result_string:
            final_result = "None"
            pattern_string = r"(https://msdn.microsoft.com/en-us/library/windows/).*"
            pattern = re.compile(pattern_string)
            found = pattern.search(result)
            if found is not None:
                url_result = result.split("'")
                final_result = url_result[1]
                print(final_result)
                break
        # Returns the description for the function
        description = find_description.find_description(final_result, function)
        # Writes the function and description in a csv file
        write_file.write_file(original_function, description)

match_functions()
