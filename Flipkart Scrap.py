#!/usr/bin/env python
# coding: utf-8

# # Scrapped Famous E-commerce website 'Flipcart'
# # In Flipcart Website we Scrapped 'Famous DSLR Cameras'
# # Scrapped Product Name,Price,Ratings and Reviews,Lens Quality,Stars
# # After succesuffuly scraping Our Data is ready for Analysis.
# '

# In[350]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import pandas as pd
#Importing Liberaries Required for our Projects


# In[351]:


webpage=requests.get('https://www.flipkart.com/search?sid=jek%2Cp31%2Ctrv&otracker=CLP_Filters&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&page=1').text
#By using Requests library we are hiting request to fetch the data from url in text format


# In[352]:


soup=BeautifulSoup(webpage,'lxml')
#Creating Soup object and passing here webpage link and format


# In[353]:


print(soup.prettify())
#Here it is our soup html Contents look like.


# # we have to scrape the data from all the pages.So we will write a code for that.
# 

# In[362]:


#Creating Lists
name=[]           #Name of Camera
stars=[]          #stars out of 5.0
price=[]          #current Price of camera
original_price=[] #original Price of camera
lens_quality=[]   # lens Quality 
ratings=[]        #Ratings of product 
review=[]         #Review of 

#WE will create that will iterate over the all the pages and add data to list
#here number of pages are 


# In[363]:


for j in range(1,5):
    webpage=requests.get('https://www.flipkart.com/search?sid=jek%2Cp31%2Ctrv&otracker=CLP_Filters&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&page={}'.format(j)).text
    soup=BeautifulSoup(webpage,'lxml')
    
    #Here we are creating Container objects.There are 24 containers in one page usally.
    #From within than container we will extracts useful Data
    cameras=soup.find_all('div',class_='_2kHMtA')

    
    #Iterate over the COntainer Object
    for i in cameras:
        try:
            name.append(i.find('div', attrs={'class':'_4rR01T'}).text.strip())
        except:
            #If any values is not present then filling with NAN
            name.append(np.nan)

        try:
            stars.append(i.find('div',attrs={'class':'_3LWZlK'}).text.strip())
            
        except:
            stars.append(np.nan)
   
        try:
            price.append(i.find('div',attrs={'_30jeq3 _1_WHN1'}).text.replace(',','').replace('₹',' ').strip())
        except:
            price.append(np.nan)

        try:
            original_price.append(i.find('div',attrs={'_3I9_wc _27UcVY'}).text.replace(',','').replace('₹',' ').strip())
        except:
            original_price.append(np.nan)
            
            
        try:
            lens_quality.append(i.find_all('li',class_='rgWa7D')[3].text)
        except:
            lens_quality.append(np.nan)
            
            
        try:
            rating=i.find('span',{'class':'_2_R_DZ'})
            ratrev=re.findall('\d+,?\d*',rating.text)
            ratings.append(ratrev[0].replace(',',''))
            
        except:
              ratings.append(np.nan)
                
                
        try:
            rating=i.find('span',{'class':'_2_R_DZ'})
            #ratings Aand reviews are in same container 'span'
            #so extracting rating and reviews seprately
            ratrev=re.findall('\d+,?\d*',rating.text)
            review.append(ratrev[1].replace(',',''))
            
        except:
            review.append(np.nan)

  
   


# In[364]:


#Creating a Data Frame
df=pd.DataFrame({'name':name,
    'stars':stars,
    'price':price,
    'OriginalPrice':original_price,
    'Quality':lens_quality,
    'Rating':ratings,
    'Reviews':review,
    })   


# In[365]:


df
#There are total 76 Items in link so we extracted all the Items


# In[368]:


df.to_csv('scrapped_data.csv')  


# In[372]:


d=df.to_dict('index')


# In[374]:


import csv
with open('csvstore.csv','w') as f:
    w = csv.writer(f)
    w.writerows(d.items())


# In[ ]:




