# Description: This program uses an artificial recurrent neural network called Long Short Term Memory (LSTM)
#               to predict the closing stock price of USDZAR H1 chart using the past 60 hours.

# Import the libraries
import math
#
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# check the data
df = pd.read_csv('USDZAR60.csv')
# print(df.head())

# Get the number of rows and columns in the data set
# print(df.shape)

# Visualize the closing price
plt.figure(figsize=(16, 9))
plt.title('Close Price History')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USDZAR', fontsize=18)
plt.show()
