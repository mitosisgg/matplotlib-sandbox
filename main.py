import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

stock_df = pd.read_csv('stock_data.csv')

stock_df.plot(x = 'Date', y = 'FB', label = 'FB',  figsize = (15, 10), linewidth = 3) 
plt.ylabel('Price ($)')
plt.xlabel('Date')
plt.title('Stock Price')
plt.grid()

stock_df.plot(x = 'Date', y = 'NFLX', label = 'NFLX',  figsize = (15, 10), linewidth = 3, color = 'red') 
plt.ylabel('Price ($)')
plt.xlabel('Date')
plt.title('Stock Price')
plt.grid()

stock_df.plot(x = 'Date', y = 'TWTR', label = 'TWTR',  figsize = (15, 10), linewidth = 3, color = 'green') 
plt.ylabel('Price ($)')
plt.xlabel('Date')
plt.title('Stock Price')
plt.grid()

plt.show()