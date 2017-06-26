from prices import get_prices

# Leave out url param to load local sample data
prices = get_prices()

#make some assertions based on local sample data
assert type(prices) == list
assert len(prices) == 20
assert prices[-2] == 3495

#pass the test
print "get_prices() local test: pass"
