import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

def plot_line_charts():
    stock_df.plot(x = 'Date', y = ['NFLX', 'FB'],  figsize = (15, 10), linewidth = 3) 
    plt.ylabel('Price ($)')
    plt.xlabel('Date')
    plt.title('Stock Prices')
    plt.grid()

    plt.show()

def plot_scatter_plot():
    X = daily_return_df['FB']
    Y = daily_return_df['NFLX']
    plt.figure(figsize = (15, 10))
    plt.scatter(X, Y)
    plt.grid()
    plt.show()

def plot_pie_chart():
    values = [20, 55, 5, 17, 3]
    colors = ['g', 'r', 'y', 'b', 'm']
    explode = [0, 0, 0, 0, 0.2]
    labels = ['AAPL', 'GOOG', 'T', 'TSLA', 'AMZN']

    plt.figure(figsize = (10, 10))
    plt.pie(values, explode, labels, colors)
    plt.title('STOCK PORTFOLIO')
    plt.show()

def plot_histogram():
    mu = round(daily_return_df['FB'].mean(), 2)
    sigma = round(daily_return_df['FB'].std(), 2)
    num_bins = 40

    plt.figure(figsize = (15,9))
    plt.hist(daily_return_df['FB'], num_bins, facecolor = 'blue')
    plt.grid()
    plt.title('Histogram: mu = ' + str(mu) + ' sd = ' + str(sigma))
    plt.show()



if __name__ == '__main__':
    # read data
    stock_df = pd.read_csv('data/stock_data.csv')
    daily_return_df = pd.read_csv('data/stocks_daily_returns.csv')

    plot_line_charts()
    plot_scatter_plot()
    plot_pie_chart()
    plot_histogram()
    