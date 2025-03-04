import streamlit as st
from chatbot_logic import get_domains, get_products, generate_insights

# Streamlit UI
st.title(" AI-driven Business Analytics Assistant")
st.write("Select a business domain and product to get insights.")

# Select Domain
domains = get_domains()
domain = st.selectbox("Select a Business Domain", domains)

# Select Product
if domain:
    products = get_products(domain)
    product = st.selectbox("Select a Product/Service", products)

    # Generate Insights
    if product:
        insights = generate_insights(domain, product)

        if insights and isinstance(insights, dict):
            # Display KPIs
            st.header(" Recommended KPIs")
            for kpi_name, kpi_impact in insights["KPIs"]:
                st.write(f"**{kpi_name}**: {kpi_impact}")

            # Display Reports
            st.header(" Suggested Reports")
            for report_name, report_use in insights["Reports"]:
                st.write(f"**{report_name}**: {report_use}")

            # Display Tools
            st.header(" Recommended Tools & Technologies")
            for tool_name, tool_purpose in insights["Tools"]:
                st.write(f"**{tool_name}**: {tool_purpose}")

            # Display Explanation for Stakeholders
            st.header(" Explanation for Stakeholders")
            st.write(insights["Explanation"])
        else:
            st.error("No data available for the selected product.")
