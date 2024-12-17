import pandas as pd
import numpy as np
from pynance import get_data
import talib

def calculate_indicators(data):
  # Calculate moving averages
  data['SMA'] = talib.SMA(data['Close'], timeperiod=30)
  data['EMA'] = talib.EMA(data['Close'], timeperiod=30)
  
  # Calculate RSI
  data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
  
  # Calculate MACD
  data['MACD'], data['MACD_signal'], data['MACD_hist'] = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
  
  return data

def get_financial_metrics(ticker):
  # Get financial data using PyNance
  financial_data = get_data(ticker)
  return financial_data

def visualize_data(data):
  import matplotlib.pyplot as plt
  
  plt.figure(figsize=(14, 7))
  
  # Plot closing price
  plt.subplot(2, 1, 1)
  plt.plot(data['Close'], label='Close Price')
  plt.plot(data['SMA'], label='SMA')
  plt.plot(data['EMA'], label='EMA')
  plt.title('Stock Price and Moving Averages')
  plt.legend()
  
  # Plot RSI
  plt.subplot(2, 1, 2)
  plt.plot(data['RSI'], label='RSI')
  plt.axhline(70, color='r', linestyle='--')
  plt.axhline(30, color='r', linestyle='--')
  plt.title('Relative Strength Index')
  plt.legend()
  
  plt.tight_layout()
  plt.show()
  
  plt.figure(figsize=(14, 7))
  
  # Plot MACD
  plt.plot(data['MACD'], label='MACD')
  plt.plot(data['MACD_signal'], label='MACD Signal')
  plt.bar(data.index, data['MACD_hist'], label='MACD Histogram')
  plt.title('MACD')
  plt.legend()
  
  plt.tight_layout()
  plt.show()

# Example usage
if __name__ == "__main__":
  ticker = 'AAPL'
  data = get_financial_metrics(ticker)
  data = calculate_indicators(data)
  visualize_data(data)
