import pandas as pd
from textblob import TextBlob

def analyze_correlation(news_df, stock_df):
  # Normalize timestamps with specific formats
  news_df['date'] = pd.to_datetime(news_df['date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce')
  stock_df['Date'] = pd.to_datetime(stock_df['Date'], format='%Y-%m-%d', errors='coerce')

  # Drop rows with invalid dates
  news_df.dropna(subset=['date'], inplace=True)
  stock_df.dropna(subset=['Date'], inplace=True)

  # Ensure unique date values
  news_df.drop_duplicates(subset=['date'], inplace=True)
  stock_df.drop_duplicates(subset=['Date'], inplace=True)

  # Convert stock_df 'Date' to UTC timezone
  stock_df['Date'] = stock_df['Date'].dt.tz_localize('UTC')

  # Set the date columns as the index
  news_df.set_index('date', inplace=True)
  stock_df.set_index('Date', inplace=True)

  # Ensure both DataFrames have the same timezone
  news_df.index = news_df.index.tz_convert('UTC') if news_df.index.tz else news_df.index.tz_localize('UTC')
  stock_df.index = stock_df.index.tz_convert('UTC') if stock_df.index.tz else stock_df.index.tz_localize('UTC')

  # Concatenate the DataFrames along the columns
  merged_df = pd.concat([news_df, stock_df], axis=1, join='inner')

  # Sentiment Analysis
  merged_df['sentiment'] = merged_df['headline'].apply(lambda text: TextBlob(text).sentiment.polarity)

  # Calculate Daily Stock Returns
  merged_df['daily_return'] = merged_df['Close'].pct_change()

  # Drop NaN values created by pct_change
  merged_df.dropna(subset=['daily_return'], inplace=True)

  # Correlation Analysis
  correlation = merged_df['sentiment'].corr(merged_df['daily_return'])

  return correlation
