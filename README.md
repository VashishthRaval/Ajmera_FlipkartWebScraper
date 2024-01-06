# Ajmera_FlipkartWebScraper
<h1>Overview</h1>
**Overview**   
This Python script is a web scraper designed to extract details from Flipkart's search results on the search query "iPhone". It retrieves information such as product name, price, and ratings for each item listed on the search page. The scraped data is then organized and stored in a CSV file for further analysis.  

**Features**  
Web Scraping: Utilizes the BeautifulSoup library to parse HTML and extract relevant information.  
Pagination Handling: Iterates through multiple pages of search results to capture a comprehensive dataset.  
CSV Data Storage: Organizes extracted data and saves it in a structured CSV file for easy analysis.  

**Usage**  
Clone the Repository:   
git clone https://github.com/your-username/flipkart-scraper.git  
cd flipkart-scraper  

Install Dependencies:  
pip install beautifulsoup4 requests  

Run the Script:  
python flipkart_scraper.py  

Check the Generated CSV File:  
The scraped data will be saved in a file named "iPhone.csv" in the same directory.
