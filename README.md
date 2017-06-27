# renthop-manager-price-scrape

### As requested by L.L.
A simple script to scrape all listing prices from a RentHop manager page (single page) and sort them, then return array

### Function 
#### get_prices(url=None) 
The `get_prices` function takes one parameter `url` as `str` (RentHop manager url) 

_If no `url` is passed to `get_prices` function, it will automatically load the content from `./test/local.html`_ 

### Usage
```python
>>> from prices import get_prices
>>> p = get_prices()
>>> print "Total ad prices scraped:", len(p)
Total ad prices scraped: 20
>>> print 'Price array:', p
Price array: [1775, 1899, 1900, 2050, 2075, 2130, 2150, 2195, 2200, 2225, 2295, 2500, 2575, 2750, 2775, 2795, 2800, 2900, 3495, 14250]
>>> print 'Second highest price:', p[-2]
Second highest price: 3495
```
