from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#this part opens a chrome browser
driver = webdriver.Chrome("C:/Users/NtMni/OneDrive/Desktop/chromedriver.exe")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

#now open the website you want to scrape
driver.get("https://www.flipkart.com/apple-macbook-air-core-i5-5th-gen-8-gb-128-gb-ssd-mac-os-sierra-mqd32hn-a-a1466/p/itmevcpqqhf6azn3?pid=COMEVCPQBXBDFJ8C&lid=LSTCOMEVCPQBXBDFJ8C4V6AHG&marketplace=FLIPKART&spotlightTagId=BestsellerId_6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=fdf3f723-b6b5-47f6-b5b9-9fd11254a315.COMEVCPQBXBDFJ8C.SEARCH&ppt=browse&ppn=browse")

#the data we want is found in the div tags of the webpage. So we find the div tags with the respective class names, extract the data and store it in a variable

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'aMaAEs'}):
    name=a.find('div', attrs={'class':'B_NuCI'})
    price=a.find('div', attrs={'class':'_30jeq3_16Jk6d'})
    rating=a.find('div', attrs={'class':'_3LWZ1K'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)


df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

