import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock_data.csv", parse_dates=['Date'], index_col='Date')

df['Daily Return A'] = df['StockA'].pct_change()
df['Daily Return B'] = df['StockB'].pct_change()

df['Cumulative Return A'] = (1 + df['Daily Return A']).cumprod()
df['Cumulative Return B'] = (1 + df['Daily Return B']).cumprod()

df[['StockA', 'StockB']].plot(title="Stock Prices")
plt.show()

df[['Daily Return A', 'Daily Return B']].plot(title="Daily Returns")
plt.show()

df[['Cumulative Return A', 'Cumulative Return B']].plot(title="Cumulative Returns")
plt.show()
