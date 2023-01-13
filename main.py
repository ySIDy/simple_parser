import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

target_url = "https://www.booking.com/"
target2 = "https://www.booking.com/searchresults.html?aid=2230186&dest_id=-1040233&dest_type=city&group_adults=3&req_adults=2&no_rooms=1&group_children=null&req_children=null"
page = requests.get(target2)

def main():
    if page.status_code == 200:
        print(page.text)
        soup = bs(page.text, "html.parser")
        h1 = soup.find_all('h1', class_="e1f827110f d5f78961c3")
        print(h1.text)
        for name in h1:
            print(name.a['title'])

if __name__ == "__main__":
    main()
    

d = "https://[domain]/[version]</[xml or json]>/[endpoint]?[parameters]"
# dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=null&req_children=null
# https://www.booking.com/
# searchresults.html 
# ?aid=2230186&dest_id=-1040233
# &dest_type=city 
# &group_adults=2 || количество людей 
# &req_adults=2 
# &no_rooms=1  || количество комнат
# &group_children=null || приспособлено для детей
# &req_children=null || 