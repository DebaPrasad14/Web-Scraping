import requests
from bs4 import BeautifulSoup
import pandas as pd


req = requests.get("https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html") # getting web page
content = req.content  # getting contents of the above link
soup = BeautifulSoup(content,"html.parser")  # parsing through html parser

elements = soup.find_all('span',{'class':'short-desc'})  # creating soup object
records = []

for element in elements:
    date = element.find('strong').text + ',2017'    # gettig date
    lie = element.contents[1][1:-2]                 # getting lie texts
    explanation = element.find('a').text[1:-1]      # fetching lie explanation
    url = element.find('a')['href']                 # fetching url of that explanation
    records.append([date,lie,explanation,url])      # storing all details in a list


df = pd.DataFrame(records, columns=['Date', 'Lie', 'Explanation', 'URL'])  # make data to tabular form
# df             --> to show data in tabular form then uncomment df
df.to_csv('Trump_lies.csv', index = False, encoding='utf-8-sig')   # export to csv file
