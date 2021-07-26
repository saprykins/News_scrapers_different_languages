# to get the site’s HTML code into your Python script so that you can interact with it to have local html code in python-object
import requests
from bs4 import BeautifulSoup
import pandas as pd

# import time-package
from datetime import datetime

URL = "https://www.tsa-algerie.com/politique/"
# requests get html-content
page = requests.get(URL)

# html.parser make choice between html, xml. Page.content is better than page.text because of encoding
soup = BeautifulSoup(page.content, "html.parser")

# results are all the articles w/ limits, lower in stack is an article
results = soup.find_all('h1', class_="title-middle")

# storage lists
titles=[]
links=[]
dates=[]

for article in results:
    title_element = article.find('a').text
    link_element = article.find('a')['href']

    #checking time from page given by a link
    page_to_get_publish_time = requests.get(link_element)
    soup = BeautifulSoup(page_to_get_publish_time.content, "html.parser")
    date_code_verb = soup.find('time', class_="article__meta-time")["datetime"]
    # date_code = date_code_verb[5:10] + ' ' + date_code_verb[11:16]
    # print(date_code, ' ', title_element)

    # adding info to our storage
    titles.append(title_element)
    links.append(link_element)

    # deletes timezone from datestring
    date_code_verb = date_code_verb[0:-6]
    # we converts time from page to python-date
    dates.append(datetime.strptime(date_code_verb, '%Y-%m-%dT%H:%M:%S'))

# save to csv-file
df = pd.DataFrame({'Date':dates, 'Title':titles})

#sort by date
ds = df.sort_values(by="Date", ascending=False)

# save to file
ds.to_csv('tsa-news.csv', index=False, encoding='utf-8')
