"""
News scrapper extracts, translates, sorts out several algerian websites
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from googletrans import Translator


# sorts and writes down several objects to file
def write_to_file(ds_pol, ds_eco, ds_ara):
    # put several dataframes together
    frames = [ds_pol, ds_eco, ds_ara]
    ds = pd.concat(frames)
    # sort by time
    ds = ds.sort_values(by="Date", ascending=False)
    # write to file
    ds.to_csv('news.csv', index=False, encoding='utf-8')


# translates column 'Title' from Arabic to French
# it appears that after several runs of script, Google stops translation
# the issue can be solved using TunnelBear
def translate(ds_pol):
    translator = Translator()
    ds_pol_copy = ds_pol.copy(deep=True)
    ds_pol_copy['Title'] = ds_pol_copy['Title'].apply(lambda x: translator.translate(x, src='ar', dest='fr').text)
    return ds_pol_copy


# web-site www.aps.dz seems to be close for scrappers
def aps_scraper():
    pass


# scraps news titles, time and links from the first page
# selectors were checked on Aug-2021 and work well for sub-sites like https://www.tsa-algerie.com/politique/
# scraps only the first page which represents 18 titles
# arabic version located on https://www.tsa-algerie.com/ar/ isn't supported since 2020
# requires an URL to be scraped and a subject (the last only for visual purposes in file)
def tsa_scraper(URL, subj):
    #preparations to use BeautifulSoup
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('h1', class_="title-middle")

    # storage for future scraped data
    titles=[]
    links=[]
    dates=[]

    for article in results:
        title_element = article.find('a').text
        link_element = article.find('a')['href']

        # checks publishing time since date isn't provided on the page
        page_to_get_publish_time = requests.get(link_element)
        soup = BeautifulSoup(page_to_get_publish_time.content, "html.parser")
        date_code_verb = soup.find('time', class_="article__meta-time")["datetime"]

        # a variation of date-cut
        # date_code = date_code_verb[5:10] + ' ' + date_code_verb[11:16]

        # add data to our storage
        titles.append(title_element)
        links.append(link_element)

        # deletes timezone from date
        date_code_verb = date_code_verb[0:-6]

        # converts time from page-friendly date to python-friendly-date
        dates.append(datetime.strptime(date_code_verb, '%Y-%m-%dT%H:%M:%S'))

    # saves to data-frame
    return pd.DataFrame({'Date':dates, 'Subj':subj, 'Title':titles})


# put together different scrapers
def etl():
    # choice of links with subjects
    URL1 = "https://www.tsa-algerie.com/politique/"
    subj1 = 'Pol'
    URL2 = "https://www.tsa-algerie.com/economie/"
    subj2 = 'Eco'
    URL3 = "https://www.tsa-algerie.com/ar/"
    subj3 = 'Ara'

    # returns dataFrames
    p_politics = tsa_scraper(URL1, subj1)
    p_econimics = tsa_scraper(URL2, subj2)
    p_ara = tsa_scraper(URL3, subj3)

    # returns translation
    p_ara_translated = translate(p_ara)

    write_to_file(p_politics, p_econimics, p_ara_translated)

etl()
