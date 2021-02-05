import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/We_Didn't_Start_the_Fire"

response = requests.get(url)
# print(response)

content = response.content
# print(content)

soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
# print(type(results))
# print(results.prettify())


# print(results.find_all('span', "citation needed"))

# get_citations_needed takes in a url and returns an integer
def get_citations_needed_count():
    citation_needed = []
    for item in soup.find_all(title="Wikipedia:Citation needed"):
        citation_needed.append(item)
    return citation_needed
print(get_citations_needed_count())

# get_citations_needed_report takes in a url and returns a string
# the string should be formatted with each citation needed on own line, in order found.

def get_citations_needed_report():
    pass