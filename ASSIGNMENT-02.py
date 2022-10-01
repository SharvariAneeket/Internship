#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install selenium')


# # QUESTION-01

# In[3]:


import selenium
import pandas as pd
import numpy as np
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[ ]:


driver=webdriver.Chrome(r'C:\Users\welcome\AppData\Local\Temp\Temp1_chromedriver_win32\chromedriver.exe')


# In[ ]:


driver.get('https://www.naukri.com/')


# In[ ]:


designation=driver.find_element(By.CLASS_NAME,'suggestor-input')
designation.send_keys('Data Analyst')


# In[ ]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div[1]/div[5]/div/div/div/input')
location.send_keys('Bangalore')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)    


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


df=pd.DataFrame({'Job_title':job_title,'Job_location':job_location,'Company_name':company_name,'Exp_required':experience_required})
df


# # QUESTION-02

# In[ ]:


driver=webdriver.Chrome(r'C:\Users\welcome\AppData\Local\Temp\Temp1_chromedriver_win32\chromedriver.exe')


# In[ ]:


driver.get('https://www.naukri.com/')


# In[ ]:


designation=driver.find_element(By.CLASS_NAME,'suggestor-input')
designation.send_keys('Data Scientist')


# In[ ]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div[1]/div[5]/div/div/div/input')
location.send_keys('Bangalore')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="mt-7 companyInfo subheading lh16"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)    


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


df=pd.DataFrame({'Job_title':job_title,'Job_location':job_location,'Company_name':company_name,'Exp_required':experience_required})
df


# # QUESTION-03
# 

# In[33]:


driver=webdriver.Chrome(r'C:\Users\welcome\AppData\Local\Temp\Temp1_chromedriver_win32\chromedriver.exe')


# In[34]:


driver.get('https://www.naukri.com/')


# In[35]:


designation=driver.find_element(By.CLASS_NAME,'suggestor-input')
designation.send_keys('Data Scientist')


# In[36]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div[1]/div[5]/div/div/div/input')
location.send_keys('Delhi/NCR')


# In[27]:


salary=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
salary.send_keys('3-6 lakhs')


# In[28]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[38]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[39]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)    


# In[40]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[41]:


df=pd.DataFrame({'Job_title':job_title,'Job_location':job_location,'Company_name':company_name,'Exp_required':experience_required})
df


# # QUESTION-04

# In[60]:


driver=webdriver.Chrome(r'C:\Users\welcome\AppData\Local\Temp\Temp1_chromedriver_win32\chromedriver.exe')


# In[63]:


driver.get('https://www.flipkart.com/')


# In[64]:


Product=driver.find_element(By.CLASS_NAME,"_3704LK")
Product.send_keys('Sunglasses')


# In[65]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[66]:


Brands=[]
Product_Description=[]
Price=[]
Discount_offered=[]


# In[84]:


start=0
end=3
for page in range(start,end):
    Brands=driver.find_elements(By.XPATH,'//div[@class='_2WkVRV']')
    for i in Brands:
        Brands.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[69]:


for page in range(start,end):
    Product_Description=driver.find_elements(By.XPATH,'//span[@class="B_NuCI"]')
    for i in Product_Description:
        Product_Description.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[71]:


len(Product_Description)


# In[70]:


for page in range(start,end):
    Price=driver.find_elements(By.XPATH,'//div[@class="_25b18c"]')
    for i in Price:
        Price.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[67]:


for page in range(start,end):
    Discount_offered=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
    for i in Discount_offered:
        Discount_offered.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)
        


# In[ ]:


print(len(Brands),len(Product_Description),len(Price),len(Discount_offered))


# In[ ]:


df=pd.DataFrame({'Brands':Brands,'Product_Description':Product_Description,'Price':Price,'Discount_offered':Discount_offered})
df


# # QUESTION-05

# In[74]:


driver=webdriver.Chrome(r'C:\Users\welcome\AppData\Local\Temp\Temp1_chromedriver_win32\chromedriver.exe')


# In[75]:


driver.get('https://www.flipkart.com/')


# In[76]:


Product=driver.find_element(By.CLASS_NAME,"_3704LK")
Product.send_keys('iphone 11')


# In[77]:


search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()


# In[86]:


Name=[]
Rating=[]
Review_summary=[]
Full_review=[]


# In[87]:


start=0
end=3
for page in range(start,end):
    Name=driver.find_elements(By.XPATH,'//div[@class="col col-7-12"]')
    for i in Name:
        Name.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)


# In[ ]:




