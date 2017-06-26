# renthop-manager-price-scrape

### As requested by Lee Lin (RentHop)
A simple script to scrape all listing prices from a RentHop manager page (single page) and sort them, then output 1) entire price array 2) second highest priced listing scraped.

### Function 

#### get_prices(url=None) 

The `get_prices` function takes one parameter `url` as `str` (STRING)
     
If no `url` is passed to `get_prices` function, it will automatically load the content from `./test/local.html`
