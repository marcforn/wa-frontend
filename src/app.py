import os
import tomllib

import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_version_info():
    try:
        with open(os.path.join(os.path.dirname(__file__), "..", "pyproject.toml"), "rb") as f:
            data = tomllib.load(f)
            version = data.get("project", {}).get("version", "Unknown")

        return version
    except FileNotFoundError:
        return "Unknown", "Unknown"


version = get_version_info()

st.set_page_config(
    page_title="Wealth Assistant",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'about': f'''**💰 Wealth Assistant v{version}**
        A comprehensive wealth management application for tracking portfolios, analyzing investments, and managing financial assets.
        '''
    }
)

pages = {
    "Portfolio": [
        st.Page(
            page="pages/portfolio/portfolio_overview_page.py",
            title="Overview",
            icon="💼",
            url_path="portfolio_overview",
        ),
        st.Page(
            page="pages/portfolio/portfolio_cash_page.py",
            title="Cash",
            icon="💵",
            url_path="portfolio_cash",
        ),
        st.Page(
            page="pages/portfolio/portfolio_index_funds_page.py",
            title="Index Funds",
            icon="🗃",
            url_path="portfolio_index_funds",
        ),
        st.Page(
            page="pages/portfolio/portfolio_retirement_plan_page.py",
            title="Retirement Plan",
            icon="🔐",
            url_path="portfolio_retirement_plan",
        ),
        st.Page(
            page="pages/portfolio/portfolio_stocks_page.py",
            title="Stocks",
            icon="📈",
            url_path="portfolio_stocks",
        ),
        st.Page(
            page="pages/portfolio/portfolio_crypto_page.py",
            title="Crypto",
            icon="🌖",
            url_path="portfolio_crypto",
        ), st.Page(
            page="pages/portfolio/portfolio_reits_page.py",
            title="REITs",
            icon="🏘",
            url_path="portfolio_reits",
        ),
    ],
    "Analyzers": [
        st.Page(
            page="pages/analyzer/reit_analyzer_page.py",
            title="REITs Analyzer",
            icon="🏘",
            url_path="reit_analyzer",
        ),
        st.Page(
            page="pages/analyzer/stock_analyzer_page.py",
            title="Stocks Analyzer",
            icon="📈",
            url_path="stock_analyzer",
        ),
    ],
}

pg = st.navigation(pages=pages, position="sidebar")

pg.run()

# Display app version
st.sidebar.caption(f"v{version}")
