def read_file(filename):
    infile = open(filename, 'r')
    infile.readline()  # read column headings
    dates = [];  prices = []
    for line in infile:
        columns = line.split(',')
        date = columns[0]
        date = date[:-3]  # skip day of month
        price = columns[-1]
        dates.append(date)
        prices.append(float(price))
    infile.close()
    dates.reverse()
    prices.reverse()
    return dates, prices

import sys
import matplotlib.pyplot as plt

dates = {};  prices = {}

for fileName in sys.argv[1:]:
    d, p = read_file(fileName)
    dates[fileName[:-4]] = d;  prices[fileName[:-4]] = p

data = {'prices': prices, 'dates': dates}

# Normalize prices
for price in prices:
    norm_price = prices[price][0]
    prices[price] = [p/norm_price for p in prices[price]]

companies = []

for fileName in sys.argv[1:]:
    plt.plot(data['prices'][fileName[:-4]])
    companies.append(fileName[:-4])

plt.legend(companies, loc=2)
plt.ylabel('Stock price')
plt.xlabel('Time')
plt.show()