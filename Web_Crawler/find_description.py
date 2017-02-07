import requests
from bs4 import BeautifulSoup


def find_description(url, function):
    if url is 'None':
        return 'None'
    else:
        # requests url and retrieves the page code
        selected_url = url
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # check to ensure the title of the page matches the function, if it matches, returns the description in p tag.
        title = str(soup.find('title'))
        if function.lower() in title.lower():
            description = (soup.find('p'))
            description = description.get_text()
            print(description)
            return(description)

        else:
            return("None")
