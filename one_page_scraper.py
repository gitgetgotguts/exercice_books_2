#HTTP request library
import requests
#  HTML parsing library
from bs4 import BeautifulSoup
# Data manipulation library
import pandas as pd


# extracting the HTML content of the page 1
response=requests.get("https://books.toscrape.com/catalogue/page-1.html")

#turning the html content into a BeautifulSoup object
soup=BeautifulSoup(response.content,"html.parser")

#finding all book containers on the page 1


# extract the ol with class "row"
ol=soup.find_all(name="ol",class_="row")






# extract all the li elements within
books=ol.find_all(name="li")

# create empty lists to store the data
data=[]
for book in books:
    book_data=dict()
    # extract the title
    title=book.article.h3.a.text
    book_data["title"]=title
    # extract the price
    price=book.find(name='p',class_="price_color").text
    book_data["price"]=price
    data.append(book_data)

# turning the dict into a dataframe
df=pd.DataFrame(data)
df.to_csv("books.csv",index=False)





