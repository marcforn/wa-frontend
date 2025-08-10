import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.set_page_config(
    page_title="Wealth Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

def fetch_reits_health():
    """Fetch health status from REITs service"""
    reits_service_url = os.getenv("REITS_URL")
    if not reits_service_url:
        st.warning("REITS_URL environment variable is not set.")
        return None

    url = f"{reits_service_url.rstrip('/')}/health"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"REITs service request failed: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error connecting to REITs service: {e}")
        return None


def reits_page():
    """REITs page with investment opportunities and analysis"""
    st.header("🏢 REITs Investment Opportunities")

    # Service health check
    with st.expander("Service Status"):
        health_data = fetch_reits_health()
        if health_data:
            st.success("REITs service is running")
            st.json(health_data)
        else:
            st.error("REITs service is not available")

    # REITs content sections
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Market Overview")
        st.metric("Total REITs", "150+", "↗️ +5%")
        st.metric("Average Yield", "4.2%", "↗️ +0.3%")
        st.metric("Market Cap", "$1.2T", "↗️ +2.1%")

        st.subheader("🏆 Top Performers")
        st.write("• **PLD** - Prologis Inc (+15.2%)")
        st.write("• **AMT** - American Tower (+12.8%)")
        st.write("• **CCI** - Crown Castle (+11.5%)")

    with col2:
        st.subheader("💡 Investment Strategies")
        st.write("• **Sector Diversification**")
        st.write("• **Geographic Spread**")
        st.write("• **Yield vs Growth Balance**")

        st.subheader("🔍 Analysis Tools")
        if st.button("Run REIT Screener"):
            st.info("REIT screening functionality coming soon...")

        if st.button("Portfolio Analysis"):
            st.info("Portfolio analysis tools coming soon...")


def stocks_page():
    """Stocks page with equity investment opportunities"""
    st.header("📈 Stocks & Equities")

    # Placeholder for stocks service integration
    st.info("Stocks service integration coming soon...")

    # Stocks content sections
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Market Indices")
        st.metric("S&P 500", "4,850.43", "↗️ +0.8%")
        st.metric("NASDAQ", "15,628.95", "↗️ +1.2%")
        st.metric("DOW", "38,790.68", "↗️ +0.5%")

        st.subheader("🔥 Trending Stocks")
        st.write("• **NVDA** - NVIDIA (+8.5%)")
        st.write("• **TSLA** - Tesla (+5.2%)")
        st.write("• **AAPL** - Apple (+2.1%)")

    with col2:
        st.subheader("💡 Investment Themes")
        st.write("• **Technology Growth**")
        st.write("• **Value Opportunities**")
        st.write("• **Dividend Aristocrats**")

        st.subheader("🔍 Stock Analysis")
        if st.button("Stock Screener"):
            st.info("Stock screening functionality coming soon...")

        if st.button("Technical Analysis"):
            st.info("Technical analysis tools coming soon...")





def main():
    pages = {
        "Portfolio": [
            st.Page(
                page="pages/portfolio_overview_page.py",
                title="Overview",
                icon="💼",
                url_path="portfolio_overview",
            ),
            st.Page(
                page="pages/portfolio_cash_page.py",
                title="Cash",
                icon="💵",
                url_path="portfolio_cash",
            ),
            st.Page(
                page="pages/portfolio_index_funds_page.py",
                title="Index Funds",
                icon="🗃",
                url_path="portfolio_index_funds",
            ),
            st.Page(
                page="pages/portfolio_retirement_plan_page.py",
                title="Retirement Plan",
                icon="🔐",
                url_path="portfolio_retirement_plan",
            ),
            st.Page(
                page="pages/portfolio_stocks_page.py",
                title="Stocks",
                icon="📈",
                url_path="portfolio_stocks",
            ),
            st.Page(
                page="pages/portfolio_crypto_page.py",
                title="Crypto",
                icon="🌖",
                url_path="portfolio_crypto",
            ),st.Page(
                page="pages/portfolio_reits_page.py",
                title="REITs",
                icon="🏘",
                url_path="portfolio_reits",
            ),
        ],
        "REITs": [
            st.Page(
                page="pages/portfolio_overview_page.py",
                title="REITs Analyzer",
                icon="📞️",
                url_path="phone_call_analyzer2",
            ),
        ],
        "Stocks": [
            st.Page(
                page="pages/portfolio_overview_page.py",
                title="Stocks Analyzer",
                icon="📞️",
                url_path="phone_call_analyzer3",
            ),
        ],
    }

    pg = st.navigation(pages)
    pg.run()

if __name__ == "__main__":
    main()
