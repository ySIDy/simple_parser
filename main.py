import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re


target2 = "https://rozetka.com.ua/notebooks/c80004/"
page = requests.get(target2)



def open_file(text):
    with open('test.txt', 'a') as f:
        f.write(text)


def main():
    if page.status_code == 200:
        # print(page.text)
        soup = bs(page.content, "html.parser")
        h1 = soup.find_all(class_="goods-tile__price-value")
        
        # print(h1)
        for data in h1:
            # if data.find('span', class_='time2 time3') is not None:
                print(data.text)

if __name__ == "__main__":
    main()
    


