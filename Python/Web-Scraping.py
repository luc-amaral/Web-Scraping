#This code save the mains news title on respective site

#!conda install requests
#!conda install beautifulsoap4
#!conda install --yes bs4
#!conda install --yes pandas

import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import csv

site = 'https://www.foxnews.com/sports'

res = requests.get(site)

res.enconding = 'UTF-8'

content = res.content

soup = BeautifulSoup(content, 'html.parser')

all_news = soup.find_all(class_= "article")
 
all_news_daily = []
for news in all_news:
    if (news.find('h2')):
        #print (news.find('h2').text)
        all_news_daily.append(news.find('h2').text)

           
titles_news = pd.DataFrame(all_news_daily)

#titles_news.drop(titles_news.iloc[1:50], inplace = True, axis=1)      
        
print((titles_news))

titles_news.to_csv('news.csv', index = False) #transform dataframe to csv file
