# Daily run script to update csv files and analyze curves for buy/sell criteria.
# If a stock meets the criteria, send an email with the details and a plot to
# email addresses in a text file.

# Import packages
from pandas.io.data import DataReader
import pandas as pd
from datetime import datetime

# Directory definitions
pth = 'C:/StockGrabber/'
pth2 = 'C:/StockGrabber/following/'

stocks= open(pth+'stocks.txt','r')

for line in stocks:
    linestr= line.rstrip()
    ticker= pd.read_csv(pth2+linestr+'.csv', index_col=0)

stocks.close()    