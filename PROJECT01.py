#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# List of President of India

# In[3]:


presedent_soup=BeautifulSoup(requests.get('https://presidentofindia.nic.in/former-presidents.htm').content,"html.parser")
presedent_soup


# In[4]:


first=presedent_soup.find('div',class_="presidentListing")
first


# In[5]:


first.text


# In[8]:


term=presedent_soup.find('span',class_="terms")
term


# In[9]:


term.text


# In[12]:


Name=[]
for i in presedent_soup.find_all('div',class_="presidentListing"):
    Name.append(i.text)
Name    


# In[14]:


Term_of_office=[]
for i in presedent_soup.find_all('span',class_="terms"):
    Term_of_office.append(i.text)
Term_of_office    


# In[15]:


print(len(Name),len(Term_of_office))


# In[21]:


import pandas as pd
df=pd.DataFrame({'Name of Presidents':Name,'Term of year':Term_of_year})
df


# MOST DOWNLOADED ARTICLES FROM AI IN LAST 90 DAYS

# In[26]:


article_soup=BeautifulSoup(requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles").content,"html.parser")
article_soup


# In[27]:


title1=article_soup.find('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR")
title1


# In[28]:


title1.text


# In[29]:


authors1=article_soup.find('span',class_="sc-1w3fpd7-0 pgLAT")
authors1


# In[30]:


authors1.text


# In[32]:


publisheddate1=article_soup.find('span',class_="sc-1thf9ly-2 bKddwo")
publisheddate1


# In[33]:


publisheddate1.text


# In[34]:


paperurl1=article_soup.find('a',href_="https://www.sciencedirect.com/science/article/pii/S0004370221000862")
paperurl1


# In[37]:


Paper_Title=[]
for i in article_soup.find_all('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    Paper_Title.append(i.text)
Paper_Title    


# In[38]:


Authors=[]
for i in article_soup.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
    Authors.append(i.text)
Authors   


# In[39]:


Published_Date=[]
for i in article_soup.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
    Published_Date.append(i.text)
Published_Date


# In[42]:


Paper_URL=[]
for i in article_soup.find_all('a',href="https://www.sciencedirect.com/science/article/pii/S0004370221000862"):
    Paper_URL.append(i.text)
Paper_URL 


# In[43]:


print(len(Paper_Title),len(Authors),len(Published_Date),len(Paper_URL))


# In[44]:


import pandas as pd
df=pd.DataFrame({'Paper Title':Paper_title,'Authors':Authors,'Published Date':Published_Date,'Paper URL:Paper_URL'})
df


# Details of top publications from Google Scholar

# In[45]:


scholar_soup=BeautifulSoup(requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en').content,"html.parser")
scholar_soup


# In[56]:


rank=scholar_soup.find('th',class_="gsc_mvt_p")
rank


# In[57]:


rank.text


# In[58]:


publication=scholar_soup.find('th',class_="gsc_mvt_t")
publication


# In[59]:


publication.text


# In[60]:


h5index=scholar_soup.find('th',class_="gsc_mvt_n")
h5index


# In[61]:


h5index.text


# In[64]:


h5median=scholar_soup.find('span',class_="gs_ibl gsc_mp_anchor")
h5median


# In[65]:


h5index.text


# In[68]:


Rank=[]
for i in article_soup.find_all('th',class_="gsc_mvt_p"):
    Rank.append(i.text)
Rank


# In[69]:


Publication=[]
for i in article_soup.find_all('th',class_="gsc_mvt_t"):
    Publication.append(i.text)
Publication


# In[70]:


h5_index=[]
for i in article_soup.find_all('th',class_="gsc_mvt_n"):
    h5_index.append(i.text)
h5_index


# In[71]:


h5_median=[]
for i in article_soup.find_all('th',class_="gsc_mvt_n"):
    h5_median.append(i.text)
h5_median


# In[72]:


print(len(Rank),len(Publication),len(h5_index),len(h5_median))


# In[73]:


import pandas as pd
df=pd.DataFrame({'Rank':Rank,'Publication':Publication,'h5-index':h5-index,'h5-median':h5_median})
df


# In[ ]:




