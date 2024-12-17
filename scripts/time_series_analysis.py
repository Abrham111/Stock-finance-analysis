import pandas as pd
import matplotlib.pyplot as plt

def plot_time_series(df):
  df['date'] = pd.to_datetime(df['date'], errors='coerce')
  # 1. Analyze Publication Frequency Over Time
  # Drop rows with invalid dates
  df = df.dropna(subset=['date'])
  # Group by date and count the number of articles per day
  daily_counts = df['date'].dt.date.value_counts().sort_index()

# Plot the publication frequency over time
  plt.figure(figsize=(12, 6))
  daily_counts.plot()
  plt.title('Publication Frequency Over Time')
  plt.xlabel('Date')
  plt.ylabel('Number of Articles')
  plt.show()

# 2. Analyze Publishing Times

# Extract the time from the datetime column
  df['time'] = df['date'].dt.time

# Group by hour and count the number of articles per hour
  hourly_counts = df['date'].dt.hour.value_counts().sort_index()

# Plot the distribution of publishing times
  plt.figure(figsize=(12, 6))
  hourly_counts.plot(kind='bar')
  plt.title('Distribution of Publishing Times')
  plt.xlabel('Hour of the Day')
  plt.ylabel('Number of Articles')
  plt.show()
