import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple stock price app 
shown are the stock closing price and volume of Google!
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerdf = tickerData.history(period='1d', start='2010-5-31', end = '2020-5-31')

# Plotting the "Close" data
st.line_chart(tickerdf['Close'])

# Plotting the "Volume" data
st.line_chart(tickerdf['Volume'])