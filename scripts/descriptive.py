import pandas as pd
import matplotlib.pyplot as plt

def headline_length_statistics(df):
  df['headline_length'] = df['headline'].apply(len)
  headline_length_stats = df['headline_length'].describe()
  print("Headline Length Statistics:")
  print(headline_length_stats)

def articles_per_publisher(df):
  articles_count = df['publisher'].value_counts()
  print("\nNumber of Articles per Publisher:")
  print(articles_count)

def articles_per_day_week(df):
  df['date'] = pd.to_datetime(df['date'], errors='coerce')
  df = df.dropna(subset=['date'])
  df['day_of_week'] = df['date'].dt.day_name()
  articles_count = df['day_of_week'].value_counts()
  print("\nNumber of Articles per Day of the Week:")
  print(articles_count)
  articles_count.plot(kind='bar', figsize=(10, 6))
  plt.title('Number of Articles Published per Day of the Week')
  plt.xlabel('Day of the Week (Monday to Sunday)')
  plt.ylabel('Number of Articles Published')
  plt.show()