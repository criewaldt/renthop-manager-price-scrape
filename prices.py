import requests
from bs4 import BeautifulSoup
from re import sub

# function to grab ad prices from renthop manager page (single page only)
def get_prices(url=None):
    
    prices = []

    # start requests session
    with requests.Session() as s:

        # if url passed load remote html content
        if url:
            response = s.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
        else:
            # if no url, load test html from local file
            with open('sample_data/local.html', 'r') as html:
                soup = BeautifulSoup(html.read(), 'html.parser')
        
        #get listing divs
        listings = soup.find_all("div", {"class":"search-listing"})

        #get prices and add to price array
        for listing in listings:
            divs = listing.find_all("div")
            # Must iterate over all divs + try/except because
            #  some missing listing photo/UI issues will throw
            #  errors when trying to parse prices
            for div in divs:
                _id = div.get('id')
                try:
                    #only look for prices in 'listing-LISTINGNUMBER-price' div
                    if "listing-" and "-price" in _id:
                        #regex to turn price string into integer, append to array
                        prices.append(int(sub(r'[^\d.]', '', div.text.strip())))
                except TypeError:
                    pass
        #sort the array
        prices.sort()
        return prices

if __name__ == "__main__":
    url = "https://www.renthop.com/managers/james-mercure-4"
    prices = get_prices(url)
    print "Total ad prices scraped:", len(prices)
    print 'Price array:', prices
    print 'Second highest price:', prices[-2]
