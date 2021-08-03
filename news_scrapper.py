"""
News scrapper that scraps, translates, sorts several sources websites in Algeria
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


# sorts and writes down several objects to file
def write_to_file(ds):
    ds = ds.sort_values(by="Date", ascending=False)
    ds.to_csv('news.csv', index=False, encoding='utf-8')


def translate():
    pass


def aps_scraper():
    pass


def tsa_scraper():
    URL = "https://www.tsa-algerie.com/politique/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('h1', class_="title-middle")

    titles=[]
    links=[]
    dates=[]

    for article in results:
        title_element = article.find('a').text
        link_element = article.find('a')['href']

        # checks publishing time
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

        # converts time from page to python-date
        dates.append(datetime.strptime(date_code_verb, '%Y-%m-%dT%H:%M:%S'))

    # saves to data-frame
    # df = pd.DataFrame({'Date':dates, 'Title':titles})
    return pd.DataFrame({'Date':dates, 'Title':titles})

# put together different scrapers
def etl():
    pd = tsa_scraper()
    write_to_file(pd)

etl()
