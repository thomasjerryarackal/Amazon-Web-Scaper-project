#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# Telling the libraries (BeautifulSoup and requests) ,from where we are taking the data 

# # Scraping content

# In[4]:


# Connect to websites

URL = 'https://www.amazon.in/DUDEME-Predict-Programmer-Developer-T-Shirt/dp/B08J25GNW2/ref=sr_1_3?crid=11ZBDUQNCWJFO&keywords=data%2Banalyst%2Btshirt&qid=1683035213&sprefix=data%2Banalyst%2Bt%2Caps%2C2066&sr=8-3&th=1&psc=1'

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64","Accept-Encoding": "gzip, deflate","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","DNT":"1","Connection":"close","Upgrade-Insecure-Requests": "1",}

page = requests.get(URL ,headers=header)

#Now we will be pulling the content to here

soup1 = BeautifulSoup(page.content,"html.parser")

print(soup1)


# By running the the above code ,we literally pulling th whole code to here.So what we need to to is to make it more formatable to understand for anyone and finds out which of all data we need.

# In[5]:


soup2 = BeautifulSoup(soup1.prettify(),"html.parser")


print(soup2)


# Now we have the code/content of that page .We are going to select which all content need for our process.
# To get the content from here.

# In[6]:


# we are now going to print the title and Website name of the t-shrit
title =title =soup2.find(id='productTitle').get_text()

store_name=soup2.find(id='bylineInfo').get_text()
print(title)

print(store_name)


# In[8]:


#to remove the white space
title =title.strip()[:27]

store_name=store_name.strip()
print(title)

print(store_name)


# # Create Dataset

# Now we will be creating a empty .csv file for storing the content.
# For that we have to import csv library and we need head row and data row for the dataset.

# In[10]:


import datetime

today=datetime.date.today()
print(today)


# In[11]:


import csv

#creating header row and data row

header=['Title','Store Name','Date']
data=[title,store_name,today]

#now creating csv file

with open('AmazondressDataset.csv','w', newline='',encoding='UTF8' ) as f :
    writer =csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[16]:


import pandas as pd


df=pd.read_csv(r'C:\Users\Smart\AmazondressDataset.csv')

print(df)


# In[15]:


#now we are going to appened the daata to next row


with open('AmazondressDataset.csv','a+', newline='',encoding='UTF8' ) as f :
    writer =csv.writer(f)
    writer.writerow(data)


# Like this way we can create dataset fro a website.
# Also we can get data through a peroid of time by using a function of time.

# In[17]:


def check_details():
    URL = 'https://www.amazon.in/DUDEME-Predict-Programmer-Developer-T-Shirt/dp/B08J25GNW2/ref=sr_1_3?crid=11ZBDUQNCWJFO&keywords=data%2Banalyst%2Btshirt&qid=1683035213&sprefix=data%2Banalyst%2Bt%2Caps%2C2066&sr=8-3&th=1&psc=1'

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64","Accept-Encoding": "gzip, deflate","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","DNT":"1","Connection":"close","Upgrade-Insecure-Requests": "1",}

    page = requests.get(URL ,headers=header)
    
    soup1 = BeautifulSoup(page.content,"html.parser")
    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
    
    title =title =soup2.find(id='productTitle').get_text()
    store_name=soup2.find(id='bylineInfo').get_text()
    
    title =title.strip()[:27]
    store_name=store_name.strip()
    
    import datetime

    today=datetime.date.today()
    
    import csv

    header=['Title','Store Name','Date']
    data=[title,store_name,today]

    with open('AmazondressDataset.csv','a+', newline='',encoding='UTF8' ) as f :
        writer =csv.writer(f)
        writer.writerow(data)


# In[20]:


while(True):
    check_details()
    time.sleep(5)


# Now what we are going to check the data after 5 seconds(no of row:3)

# In[21]:


import pandas as pd


df=pd.read_csv(r'C:\Users\Smart\AmazondressDataset.csv')

print(df)


# Now the row number has increased to 27.

# In[ ]:




