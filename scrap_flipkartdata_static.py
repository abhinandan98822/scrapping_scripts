from bs4 import BeautifulSoup
import requests
import pandas as pd
 
#site url
url="https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

#request to the site
req=requests.get(url)

#site content
content=BeautifulSoup(req.content,'html.parser')

#get all data from the site
data=content.find_all('div',{'class':'_2kHMtA'})

#empty lists
phone_name=[]
price=[]
links=[]

#store links where every link start from startlink
start_link="https://www.flipkart.com"

#loop to iterrate data in order from data in bulk
for items in data:
    #startlink+restlink
    rest_link=items.find('a')['href']
    #product name
    name=items.find('div',{'class':'_4rR01T'}).string
    #product price
    price=items.find('div',{'class':'_30jeq3 _1_WHN1'})
    phone_name.append(name)
    links.append(start_link+rest_link)


#data order form
dataframe={'phone_name':phone_name,'price':price,'links':links}
#order the data according to the dict or store into the columns
final_dataframe=pd.DataFrame(dataframe)
#save te-he data into csv file
final_dataframe.to_csv('datasave.csv')
