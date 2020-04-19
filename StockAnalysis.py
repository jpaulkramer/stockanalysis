#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:46:02 2020

@author: john
"""


import requests
import pandas as pd

import yfinance as yf


pg = yf.Ticker('PG')

pghist = pg.history('6mo')

pghist['SMA'] = pghist.Close.rolling(50).mean()

pghist['EMA'] = pghist.Close.rolling(10,win_type='exponential') # doesn't work for some reason.

# try df.ewm() instead? need to do more research on all the parameters.
