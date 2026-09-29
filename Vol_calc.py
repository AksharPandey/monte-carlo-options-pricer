import yfinance as yf
import numpy as np

def currentprice(ticker, period):
    x = yf.Ticker(ticker)
    y = x.history(period=period)['Open'].tolist()[-1]
    return y

def volfinder(ticker, period):
    x = yf.Ticker(ticker)
    y = x.history(period=period)['Open'].tolist()
    new_y = []
    count = 0

    for x in y:
        if count != 0:
            new_y.append(np.log(y[count]/y[count-1]))
        count += 1

    vol = np.std(new_y, ddof=1) * np.sqrt(252)

    return vol

