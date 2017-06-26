import requests
from bs4 import BeautifulSoup
from re import sub

#function to grab ad prices from renthop manager page (single page only)
def get_prices(url=None):
    
    prices = []

    #start requests session
    with requests.Session() as s:

        ### if url passed load remote html content
        if url:
            response = s.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
        ### if no url, load test html from local file
        else:
            with open('test/local.html', 'r') as html:
                soup = BeautifulSoup(html.read(), 'html.parser')
        
        #get listing divs
        listings = soup.find_all("div", {"class":"search-listing"})

        #get prices and add to price array
        for listing in listings:
            divs = listing.find_all("div")
            for div in divs:
                _id = div.get('id')
                # Must wrap this in a weird try/except because
                # some listing photo/UI issues will throw
                # weird errors when trying to parse listings
                try:
                    #only look for prices in 'listing-*-price' div
                    if "listing-" and "-price" in _id:
                        #regex to turn price string into integer so we can sort them later
                        prices.append(int(sub(r'[^\d.]', '', div.text.strip())))
                except TypeError:
                    pass
                
        #sort the array
        prices.sort()
        return prices

if __name__ == "__main__":
    url = "https://www.renthop.com/managers/pesach-azizo"
    prices = get_prices(url)

    print "Total ad prices scraped:", len(prices)
    print 'Price array:', prices
    print 'Second highest price:', prices[-2]
