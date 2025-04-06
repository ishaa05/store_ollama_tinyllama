import streamlit as st
import pandas as pd
from agents.store_agent import store_agent_response
from tools.inventory_tool import get_inventory
from tools.forecast_tool import get_forecast
from tools.forecast_tool import get_demand_forecast
st.set_page_config(page_title="📦 Store Manager Dashboard", layout="wide")

st.title("🏬 Store Manager Dashboard")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔍 Inventory", "📈 Sales Trends", "📊 Demand Forecast", "🛒 Restock Suggestions", "✉️ Request Stock"])

with tab1:
    st.header("🔍 Inventory Overview")
    st.dataframe(get_inventory())

with tab2:
    st.header("📈 Sales Trends")
    forecast_data = get_forecast()
    product_ids = forecast_data["Product ID"].unique()
    selected_id = st.selectbox("Select Product ID", product_ids)
    st.write(f"Demand Trend for Product ID {selected_id}")
    trend = forecast_data[forecast_data["Product ID"] == selected_id]
    st.line_chart(trend["Sales Quantity"])

with tab3:
    st.header("📊 Demand Forecast")

    selected_forecast_id = st.selectbox("Select Product for Forecast", product_ids, key="forecast")
    forecast_range = st.selectbox("Forecast Days", [7, 15, 30], key="forecast_days")

    forecast_df = get_demand_forecast(selected_forecast_id, days=forecast_range)

    if isinstance(forecast_df, dict) and "error" in forecast_df:
        st.error(forecast_df["error"])
    else:
        st.subheader("📅 Forecast Table")
        st.dataframe(forecast_df)

        st.subheader("📊 Forecast Graph")
        st.line_chart(forecast_df.set_index("Date")["Forecast Sales"])

with tab4:
    st.header("🛒 Restock Suggestions")
    selected_id = st.selectbox("Select Product for Suggestion", product_ids, key="restock")
    if st.button("💡 Get Restock Suggestion"):
        response = store_agent_response(selected_id)
        st.success(response)

with tab5:
    st.header("✉️ Request Stock")
    selected_id = st.selectbox("Select Product", product_ids, key="manual")
    qty = st.number_input("Enter Quantity", min_value=1, step=1)
    if st.button("📤 Send Manual Request"):
        from tools.restock_tool import restock_tool
        result = restock_tool(selected_id, qty)
        st.json(result)
