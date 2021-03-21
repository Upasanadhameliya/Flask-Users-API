# Task - Create API


## This repository uses python=3.8 with MongoDB version v4.4.4. The api allows users to do the following things:
  1. Make a post request where one can pass in user details in JSON format with the following details:
     ID, name, mobile number, age.
     ```
     curl --header "Content-Type: application/json" --request POST --data "{\"ID\":\"101\",\"name\":\"demo\",\"mobile number\":\"2233445566\",\"age\":\"23\"}" http://127.0.0.1:5000/
     ```
  2. Scraping https://www.sportsdirect.com/ and saving the scraped product data as a JSON file and downloading 
     specifc product image files. Tutorial source: https://youtu.be/4I6Xg6Y17qs
  3. Scraping http://quotes.toscrape.com/ to get quotes, author, tags and URL and save them in a JSON file. Tutorial source - 
     Scrapinghub: https://youtu.be/vkA1cWN4DEc

# Install
```
pip install -r requirements.txt
```

# Running the crawlers/spiders

###### FundRazr spider 
From the FundRazr directory run the following command:
```
scrapy crawl FundRazr -o <filename>.csv
```

###### SportsDirect spider 
From the simple_crawler directory run the following command:
```
scrapy crawl sportsdirect --set FEED_URI=<filename>.jl
```

###### QuotesToScrape spiders 
To run the spiders in this project, from QuotesToScrape directory run the following commands: 
```
scrapy crawl authors -o <filename>.json
```
Scrapes and saves all authors and their burthdates.


```
scrapy crawl quotes -o <filename>.json
```
Scrapes and saves all quotes with their author and tags.


```
scrapy crawl quotes_scroll -o <filename>.json
```
Scrapes and saves all quotes with their author and tags when the page uses continuous scrolling and not a Nex Page  button.


```
scrapy crawl login_spider -o <filename>.json
```
This spider first performs a login to then access a link to goodreads.com accessible only after the login. Then saves 
The atuhor and their respective page in goodreads.com

# Output

###### FundRazr spider 
![Alt text](screens/fundrazr_screen.png?raw=true "FundRazr csv")

###### SportsDirect spider 
![Alt text](screens/sportsdirect_screen.png?raw=true "SportsDirect JSON")
![Alt text](screens/sportsdirect_screen2.png?raw=true "SportsDirect Downloads")

###### authors spider 
![Alt text](screens/authors.png?raw=true "authors json")

###### quotes/quotes_scroll spider
![Alt text](screens/quotes.png?raw=true "quotes json")

###### login_spider spider
![Alt text](screens/author_goodreadurl.png?raw=true "logn_author_goodreads_url json")
