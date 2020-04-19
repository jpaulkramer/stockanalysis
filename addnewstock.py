# script to take input and add a stock history from Jan 1 2014 to the present
# day using pandas, and add a moving averages to each one.
# will create one .csv file per stock, and the stocks analyzed will be stored in
# a single text file.

# clear workspace
#clear

# Import packages
from pandas.io.data import DataReader
import pandas as pd
from datetime import datetime
#import matplotlib.pyplot as plt

# set filepath to program directory
pth = 'C:/StockGrabber/'
pth2 = 'C:/StockGrabber/following/'

# request ticker name

newstock = raw_input('Input Ticker Symbol: ')

# check if we're already following this stock
if newstock in open(pth+'stocks.txt').read():
    print('That stock is already being followed.')
else:    
    try:
        print('Grabbing stocks for ', newstock, ' from Jan 1 2014 to present.')
        stockdata = DataReader(newstock, 'yahoo', datetime(2014,1,1))
        
        print ('Adding ', newstock, ' to analysis list.')
        namefile = open(pth+'stocks.txt', 'a+')
        namefile.write(newstock+"\n")
        namefile.close()
        
        # add 50 day SMA and 10 day EMA to stock data
        sma = pd.rolling_mean(stockdata['Adj Close'], 50)
        ema = pd.ewma(stockdata['Adj Close'], span=10)
        averages = pd.concat([sma,ema], axis=1)
        stockdata = pd.concat([stockdata, averages], axis=1)
        # stockdata.rename(columns={'0':'SMA','1':'EWMA'}, inplace=True) Doesn't work for last 2 columns for some reason

        # stockdata.plot() # doesn't work???
        stockfile = open(pth2+newstock+'.csv','a+')
        stockdata.to_csv(stockfile)
        stockfile.close()
    except:
        print('Couldnt find', newstock)
