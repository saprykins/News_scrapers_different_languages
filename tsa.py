# to get the site’s HTML code into your Python script so that you can interact with it to have local html code in python-object
import requests
from bs4 import BeautifulSoup

URL = "https://www.tsa-algerie.com/politique/"
# requests get html-content
page = requests.get(URL)

# html.parser make choice between html, xml. Page.content is better than page.text because of encoding
soup = BeautifulSoup(page.content, "html.parser")

# results are all the articles w/ limits, lower in stack is an article
results = soup.find_all('h1', class_="transition")

for article in results:
    title_element = article.find('a').text
    link_element = article.find('a')['href']

    #checking time from page given by a link
    page_to_get_publish_time = requests.get(link_element)
    soup = BeautifulSoup(page_to_get_publish_time.content, "html.parser")
    date_code_verb = soup.find('time', class_="article__meta-time")["datetime"]
    date_code = date_code_verb[5:10] + ' ' + date_code_verb[11:16]
    print(date_code, ' ', title_element)
