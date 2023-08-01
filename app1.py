import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Indian Stock Price App
Enter an Indian stock symbol to see its closing price and volume!
""")

# User input for the Indian stock symbol (NSE or BSE)
tickerSymbol = st.text_input("Enter an Indian stock symbol (e.g., RELIANCE.NS)", 'RELIANCE.NS')

tickerData = yf.Ticker(tickerSymbol)

tickerdf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

if not tickerdf.empty:
    # Plotting the "Close" data
    st.write(f"Closing Price for {tickerSymbol}:")
    st.line_chart(tickerdf['Close'])

    # Plotting the "Volume" data
    st.write(f"Volume for {tickerSymbol}:")
    st.line_chart(tickerdf['Volume'])
else:
    st.write("Data not found for the given stock symbol.")
