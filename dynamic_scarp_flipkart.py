from bs4 import BeautifulSoup
import requests
import pandas as pd


search_product=input("Enter data you want to search-:")
#site url
url="https://www.flipkart.com/search?q="+search_product+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

#request to the site
req=requests.get(url)

#site content
content=BeautifulSoup(req.content,'html.parser')
# print(content.prettify)
#get all data from the site
page_content=content.find_all(True,{'class':['_13oc-S _1t9ceu','_2kHMtA','_13oc-S','_4ddWXP']})
# print(page_content,'pnn')
#datalists
product_title=[]
product_price=[]
product_image=[]
product_details=[]

# for items in page_content:
for data in page_content:
    # product_title=data.find_all(True,{'class':['_4rR01T','_2kHMtA','_13oc-S','_4ddWXP','_2WkVRV','s1Q9rs']})
    # product.append(product_title)

    #scrap the title of mobile
    M_title=data.find('div',{'class':'_4rR01T'}).string

    #scrap the price of the mobile
    M_price=data.find('div',{'class':'_30jeq3 _1_WHN1'}).string

    #scrap all div of same class containing  images
    M_image=data.find('div',{'class':'CXW8mj'})
    #scrap all img tag inside div of given class 
    for img in M_image.find_all('img',class_='_396cs4'):
        #get all src from img tag
        product_image.append(img['src'])

    #get product details by using nested scraping
    M_product_details=data.find('div',{'class':'fMghEO'})
    #scrap all li or another tag using this method
    for basic_details in M_product_details.find_all('li',class_='rgWa7D'):
        product_details.append(basic_details.text)


#APPEND all data into the given lists
    product_title.append(M_title)
    product_price.append(M_price)
