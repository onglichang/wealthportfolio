import yfinance as yf
import pandas as pd

def getEquityCurrentPrice(ticker: str) -> float:
    equity = yf.Ticker(ticker)
    return equity.info['currentPrice']

# print(getEquityCurrentPrice("SQ"))