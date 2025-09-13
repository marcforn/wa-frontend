import time

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Initialize session state for form visibility
if 'show_form' not in st.session_state:
    st.session_state.show_form = True
if 'analysis_completed' not in st.session_state:
    st.session_state.analysis_completed = False

st.title("🏘 REIT Analyzer")
st.markdown(
    """
    Welcome to the REITs Analyzer page! Here, you can explore in-depth analyses of Real Estate Investment Trusts (REITs), uncover property sector opportunities, and gain actionable insights to inform your real estate investment decisions.
    Use this page to review REIT market trends, evaluate performance, and identify potential growth areas within the real estate sector. Stay ahead with data-driven recommendations and tools designed to help you make smarter REIT investment choices.
    """
)

# Show form if it's enabled or show collapsed version with results
if st.session_state.show_form:
    with st.form("reit_analysis_form"):
        st.subheader("Property Data")

        # Location / Neighborhood
        location = st.text_input(
            "Location / Neighborhood",
            placeholder="Enter address, neighborhood, or city",
            help="Property location for market analysis and comparables"
        )

        # Purchase Price
        purchase_price = st.number_input(
            "Purchase Price (€)",
            min_value=50000,
            value=100000,
            step=500,
            help="Property purchase price"
        )

        # Renovation
        renovation = st.number_input(
            "Renovation (€)",
            min_value=0,
            max_value=100000,
            step=500,
            help="Estimated renovation cost"
        )

        # Monthly Rent
        monthly_rent = st.number_input(
            "Monthly Rent (€)",
            min_value=300,
            value=500,
            step=10,
            help="Expected monthly rental income"
        )

        st.subheader("Mortgage Data")

        # Mortgage Percentage
        mortgage_percentage = st.selectbox(
            "Mortgage (%)",
            options=[70, 80, 90, 100],
            index=0,
            help="Mortgage financing percentage"
        )

        # Mortgage Interest
        mortgage_interest = st.number_input(
            "Mortgage Interest (%)",
            min_value=0.0,
            max_value=4.0,
            step=0.1,
            value=2.5,
            help="Annual mortgage interest rate"
        )

        # Mortgage Years
        mortgage_years = st.selectbox(
            "Mortgage Years",
            options=[20, 25, 30],
            index=0,
            help="Mortgage duration in years"
        )

        st.subheader("Projections")

        # Revaluation
        revaluation = st.number_input(
            "Annual Revaluation (%)",
            min_value=0.0,
            max_value=20.0,
            step=0.1,
            value=10.0,
            help="Expected annual property revaluation percentage"
        )

        # Submit button
        submitted = st.form_submit_button(label="Analyze Investment", type="primary")

        if submitted:
            # Store form data in session state
            st.session_state.form_data = {
                'location': location,
                'purchase_price': purchase_price,
                'renovation': renovation,
                'monthly_rent': monthly_rent,
                'mortgage_percentage': mortgage_percentage,
                'mortgage_interest': mortgage_interest,
                'mortgage_years': mortgage_years,
                'revaluation': revaluation
            }

            # Show loading spinner
            with st.spinner('Analyzing investment... Please wait.'):
                time.sleep(2)  # Simulate API call delay

            # Update session state
            st.session_state.show_form = False
            st.session_state.analysis_completed = True
            st.rerun()

# Show results if analysis is completed and form_data exists
if st.session_state.analysis_completed and not st.session_state.show_form and 'form_data' in st.session_state:

    # Get data from session state
    data = st.session_state.form_data
    location = data['location']
    purchase_price = data['purchase_price']
    renovation = data['renovation']
    monthly_rent = data['monthly_rent']
    mortgage_percentage = data['mortgage_percentage']
    mortgage_interest = data['mortgage_interest']
    mortgage_years = data['mortgage_years']
    revaluation = data['revaluation']

    # Display input summary
    st.subheader("📋 Investment Summary")
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Property Details:**")
        st.write(f"• Location: {location if location else 'Not specified'}")
        st.write(f"• Purchase Price: €{purchase_price:,.2f}")
        st.write(f"• Renovation Cost: €{renovation:,.2f}")
        st.write(f"• Total Investment: €{purchase_price + renovation:,.2f}")

    with col2:
        st.write("**Financing Details:**")
        st.write(f"• Monthly Rent: €{monthly_rent:,.2f}")
        st.write(f"• Mortgage: {mortgage_percentage}% for {mortgage_years} years")
        st.write(f"• Interest Rate: {mortgage_interest}%")
        st.write(f"• Annual Revaluation: {revaluation}%")

    # Mocked Analysis Results
    st.subheader("📊 Investment Analysis Results")

    # Calculate some basic metrics for mocked data
    total_investment = purchase_price + renovation
    loan_amount = (mortgage_percentage / 100) * purchase_price
    down_payment = total_investment - loan_amount
    annual_rent = monthly_rent * 12

    # Mock calculations
    monthly_mortgage_payment = loan_amount * (mortgage_interest / 100 / 12) * ((1 + mortgage_interest / 100 / 12) ** (mortgage_years * 12)) / (((1 + mortgage_interest / 100 / 12) ** (mortgage_years * 12)) - 1)
    annual_mortgage_payment = monthly_mortgage_payment * 12
    net_annual_income = annual_rent - annual_mortgage_payment
    roi = (net_annual_income / down_payment) * 100 if down_payment > 0 else 0

    # Display results in columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="💰 Monthly Cash Flow",
            value=f"€{monthly_rent - monthly_mortgage_payment:,.0f}",
            delta=f"€{monthly_rent:,.0f} rent - €{monthly_mortgage_payment:,.0f} mortgage"
        )

    with col2:
        st.metric(
            label="📈 Annual ROI",
            value=f"{roi:.1f}%",
            delta="On initial investment"
        )

    with col3:
        st.metric(
            label="🏠 Property Value (5Y)",
            value=f"€{purchase_price * (1 + revaluation / 100) ** 5:,.0f}",
            delta=f"+€{purchase_price * (1 + revaluation / 100) ** 5 - purchase_price:,.0f}"
        )

    # Detailed breakdown
    st.subheader("💡 Investment Breakdown")

    breakdown_data = {
        "Metric": [
            "Down Payment Required",
            "Loan Amount",
            "Monthly Mortgage Payment",
            "Annual Gross Rental Income",
            "Annual Net Income (after mortgage)",
            "Cap Rate",
            "Break-even Rent"
        ],
        "Value": [
            f"€{down_payment:,.2f}",
            f"€{loan_amount:,.2f}",
            f"€{monthly_mortgage_payment:,.2f}",
            f"€{annual_rent:,.2f}",
            f"€{net_annual_income:,.2f}",
            f"{(net_annual_income / total_investment * 100):.2f}%",
            f"€{monthly_mortgage_payment + 200:,.0f}"  # Mock break-even with expenses
        ]
    }

    st.table(breakdown_data)

    # Risk Assessment (Mocked)
    st.subheader("⚠️ Risk Assessment")

    risk_score = 65  # Mock risk score
    if risk_score >= 80:
        risk_color = "🟢"
        risk_level = "Low Risk"
    elif risk_score >= 60:
        risk_color = "🟡"
        risk_level = "Medium Risk"
    else:
        risk_color = "🔴"
        risk_level = "High Risk"

    st.write(f"**Overall Risk Level:** {risk_color} {risk_level} ({risk_score}/100)")

    # Mock recommendations
    st.subheader("🎯 Recommendations")
    recommendations = [
        "✅ Positive monthly cash flow expected",
        f"⚠️ Consider negotiating purchase price below €{purchase_price * 0.95:,.0f}",
        "💡 Location shows strong rental demand",
        f"📊 ROI of {roi:.1f}% is {'above' if roi > 8 else 'below'} market average"
    ]

    for rec in recommendations:
        st.write(rec)

    # Add New Calculation button at the bottom
    st.divider()
    if st.button("🔄 New Calculation", type="secondary"):
        st.session_state.show_form = True
        st.session_state.analysis_completed = False
        st.rerun()
