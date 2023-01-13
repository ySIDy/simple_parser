import requests
from datetime import datetime

url_sample = "https://[domain]/[version]</[xml or json]>/[endpoint]?[parameters]"
url = "https://.booking.com/2</json>/hotelAvailability?[parameters]"


def url_creator() -> str:
    date = datetime.now()
    # print(date.day, date.month, date.year)
    r = requests.get(url=f"https://distribution-xml.booking.com/2.0/json/hotelAvailability?checkin={date.year}-{date.month}-{date.day}&checkout={date.year}-{date.month}-{date.day+2}&hotel_ids=4462291&room1=A,A,6&guest_country=nl&extras=hotel_details,room_details&options=show_test")
    print(r)

def main():
    url_creator()


if __name__ == "__main__":
    main()

# https://developers.booking.com/api/commercial/index.html?version=2.9&page_url=child-rate
# source