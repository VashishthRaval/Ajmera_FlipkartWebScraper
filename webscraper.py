#Importing Libraries
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

def scrape_flipkart(search_url):
    i = 1
    page_number = 1
    
    while True:
        # Forming the URL
        current_page_url = search_url + f'&page={page_number}'

        uClient = uReq(current_page_url)
        page_html = uClient.read()
        uClient.close()

        # Parsing HTML content
        page_soup = soup(page_html, "html.parser")

        # Finding all product containers
        containers = page_soup.findAll("div", {"class": "_13oc-S"})

        # Opening CSV file in append mode
        filename = "iPhone.csv"
        with open(filename, "a") as f:
            for container in containers:
                # Extracting product details
                product_name = container.div.img["alt"]

                price_container = container.findAll("div", {"class": ["_30jeq3", "_1_WHN1"]})
                price1 = price_container[0].text.lstrip('₹')
                price = "Rs. " + price1

                rating_container = container.findAll("div", {"class": "_3LWZlK"})
                rating = rating_container[0].text.strip()

                # Writing data to the CSV file
                f.write(str(i) + " , " + product_name.replace(",", " |") + " , " + price.replace(",", "") + " , " + rating + "\n")
                i += 1

        # Pagination Handling
        next_button = page_soup.find("a", {"class": "_1LKTO3"})
        if next_button and "disabled" not in next_button.attrs.get("class", []):
            page_number += 1
        else:
            break

search_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
scrape_flipkart(search_url)
