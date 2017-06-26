import requests
from bs4 import BeautifulSoup

from re import sub
from decimal import Decimal

prices = []

#start request session
with requests.Session() as s:

    ### read remote html
    """
    response = s.get('https://www.renthop.com/managers/pesach-azizo?bedrooms%5B%5D=1&bedrooms%5B%5D=2&min_price=&max_price=')
    soup = BeautifulSoup(response.content, 'html.parser')
    """
    
    ### read local html
    with open('local.html', 'r') as html:
        soup = BeautifulSoup(html.read(), 'html.parser')
        
    #get listing divs
    listings = soup.find_all("div", {"class":"search-listing"})

    #get prices and add to price array
    for listing in listings:
        divs = listing.find_all("div")
        for div in divs:
            _id = div.get('id')
            try:
                if "listing-" and "-price" in _id:
                    prices.append(int(sub(r'[^\d.]', '', div.text.strip())))
            except TypeError:
                pass

    print prices
    prices.sort()
    print prices

    print "lowest price:", prices[0]
    print "highest price:", prices[-1]
    print "second highest price:", prices[-2]
