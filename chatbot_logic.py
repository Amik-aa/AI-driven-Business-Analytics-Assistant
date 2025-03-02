import json

# Loading KPI Data
def load_kpi_data():
    """Loads KPI data from JSON file."""
    with open("kpi_data.json", "r", encoding="utf-8") as file:
        return json.load(file)

kpi_data = load_kpi_data()

# Getting available domains
def get_domains():
    """Returns available business domains."""
    return list(kpi_data.keys())

# Getting available products/services for a domain
def get_products(domain):
    """Returns available products for the given domain."""
    return list(kpi_data[domain].keys()) if domain in kpi_data else []

# Getting recommendations based on domain & product
def get_recommendations(domain, product):
    """Fetches KPIs, Reports, Tools, and Explanations for the selected domain and product."""
    if domain in kpi_data and product in kpi_data[domain]:
        return kpi_data[domain][product]
    return None

# Main function to fetch insights
def generate_insights(domain, product):
    """Generates business insights including KPIs, reports, tools, and explanations."""
    recommendations = get_recommendations(domain, product)

    if recommendations:
        insights = {
            "KPIs": [(kpi["name"], kpi["impact"]) for kpi in recommendations["KPIs"]],
            "Reports": [(report["name"], report["use"]) for report in recommendations["Reports"]],
            "Tools": [(tool["name"], tool["purpose"]) for tool in recommendations["Tools"]],
            "Explanation": recommendations["Explanation"]
        }
        return insights
    else:
        return "No data available for the selected product."

