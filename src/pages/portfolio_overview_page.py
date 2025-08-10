import asyncio

import streamlit as st
from dotenv import load_dotenv

load_dotenv()


st.title("💼 Portfolio Overview")
st.markdown(
    """Welcome to your all-in-one dashboard for monitoring the status of your entire investment portfolio. Here, you can view a consolidated summary of your assets, track performance metrics,
     and analyze allocation across different asset classes. Stay informed about your portfolio's health, recent transactions, and take action to optimize your investments."""
)

# Portfolio overview
st.subheader("📊 REITs Overview")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Value", "$125,430", "↗️ +3.2%")
with col2:
    st.metric("Daily P&L", "+$2,450", "↗️ +2.0%")
with col3:
    st.metric("Allocation", "65% Stocks", "↗️ +1%")
with col4:
    st.metric("Cash", "$15,200", "↘️ -5%")

# Asset allocation chart placeholder
st.subheader("📈 Asset Allocation")
st.info("Interactive asset allocation chart coming soon...")

# Portfolio actions
st.subheader("🛠️ Portfolio Actions")

col1, col2 = st.columns(2)
with col1:
    if st.button("Rebalance Portfolio"):
        st.info("Portfolio rebalancing tool coming soon...")

    if st.button("Risk Analysis"):
        st.info("Risk analysis dashboard coming soon...")

with col2:
    if st.button("Performance Report"):
        st.info("Performance reporting coming soon...")

    if st.button("Tax Optimization"):
        st.info("Tax optimization tools coming soon...")

# Recent transactions
st.subheader("📝 Recent Transactions")
st.write("• **Bought** 10 shares of PLD at $125.50")
st.write("• **Sold** 5 shares of NVDA at $485.20")
st.write("• **Bought** 25 shares of AAPL at $175.30")
