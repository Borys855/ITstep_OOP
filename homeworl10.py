from bs4 import BeautifulSoup

import requests
response = requests.get("https://ua.sinoptik.ua/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
soup_list = soup.find_all("div", {"class": "css-1267ixm"})

if soup_list:
        price_div = soup_list[0]
        price = price_div.find("div")

        if price:
            print(price.text)
        else:
            print("Element not found")
    else:
        print("response code is not 200")