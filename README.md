# Store Manager Dashboard

An intelligent and interactive **retail management dashboard** that uses **Machine Learning** and **LLM agents (TinyLLaMA via Ollama)** to optimize inventory decisions, forecast demand and streamline restocking operations.

---

## Features

| Feature                   | Description |
|--------------------------|-------------|
|  **Inventory Monitoring**  | Tracking of product stock from inventory data |
|  **Sales Trends**         | Line graph of historical product sales |
|  **Demand Forecasting**   | ML-based per-product demand forecasting using Linear Regression |
|  **Restock Suggestions**  | LLM (TinyLLaMA) intelligently suggests if restocking is needed |
|  **Manual Restocking**    | Option to manually place a restock request |
|  **Auto Restocking Agent** | Agent posts stock requests based on forecast and stock *(coming soon)* |
|  **Dynamic Pricing View** | Pricing updates integrated from pricing dataset *(coming soon)* |
|  **Alerts & Reports**     | Low stock, slow/fast-moving product alerts *(coming soon)* |

---

## Agent Architecture (LangChain + Ollama)

The **Store Agent** is an LLM-powered tool-using agent that makes restocking decisions by analyzing:

- Forecasted demand (via ML model)
- Current inventory (from CSV/DB)

**LLM Used:** [TinyLLaMA via Ollama](https://ollama.com/library/tinyllama)

---

## Demand Forecasting Model

Demand is predicted using **Linear Regression** trained on daily sales data. Forecasting is available for:

- Next **7 days**
- Next **15 days**
- Next **30 days**

Results are visualized for easy understanding.

---



