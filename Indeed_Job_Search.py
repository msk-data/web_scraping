#!/usr/bin/env python
# coding: utf-8

# In[74]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=data%20engineer&l=New%20York%2C%20NY&start={page}&vjk=97d70eb2f37da8d3'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def transform(soup):
    divs_title = soup.find_all('div' , class_ = 'slider_container')
    for item in divs_title:
        job_title = item.find('h2' , class_ = 'jobTitle').text
        company = item.find('span', class_ = 'companyName').text
        location = item.find('div', class_ ='companyLocation').text  
        try:
            salary = item.find('span' , class_ = 'salary-snippet').text
        except:
            salary = ''
        summary = item.find('div' , class_ = 'job-snippet').text
        
        job = {
            'job_title' : job_title,
            'company' : company,
            'location' : location,
            'salary' : salary,
            'summary' : summary
        }
        joblist.append(job)
    return
        
        
        
joblist = []    

for i in range(0,20,10):
    print(f'Getting page, {i}')
    c=extract(i)
    transform(c)
    
df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('Indeed_Jobs_Sep.csv')


# In[ ]:




