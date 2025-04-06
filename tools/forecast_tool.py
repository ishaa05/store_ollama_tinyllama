import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the full demand forecasting dataset
def get_forecast():
    return pd.read_csv("data/demand_forecasting.csv")

# Forecast future sales using Linear Regression
def get_demand_forecast(product_id, days=7):
    df = get_forecast()
    df = df[df['Product ID'] == product_id]

    if df.empty:
        return {"error": f"No data found for Product ID {product_id}"}

    # Prepare data
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.groupby('Date')['Sales Quantity'].sum().reset_index()
    df['Day'] = (df['Date'] - df['Date'].min()).dt.days

    X = df[['Day']]
    y = df['Sales Quantity']

    model = LinearRegression()
    model.fit(X, y)

    # Predict next N days
    future_days = np.array([[X['Day'].max() + i] for i in range(1, days + 1)])
    forecast = model.predict(future_days)

    forecast = [max(0, round(num)) for num in forecast]  # No negative sales
    future_dates = pd.date_range(df['Date'].max() + pd.Timedelta(days=1), periods=days)

    result_df = pd.DataFrame({
        'Date': future_dates,
        'Forecast Sales': forecast
    })

    return result_df
