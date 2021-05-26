#!/usr/bin/env python
# coding: utf-8

# In[3]:


import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Just Example
Shown are the stock closing price and volume of Facebook!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'FB'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.line_chart(tickerDf.Dividends)

# streamlit run "Put path stock_yfinance_streamlit.py"

