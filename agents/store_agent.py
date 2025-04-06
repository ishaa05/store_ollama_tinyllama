from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain_community.chat_models import ChatOllama

from tools.inventory_tool import get_stock_level
from tools.forecast_tool import get_demand_forecast
from tools.restock_tool import restock_tool

def store_agent_response(product_id):
    tools = [
        Tool(name="Inventory Lookup Tool", func=lambda _: get_stock_level(product_id), description="Check stock level"),
        Tool(name="Forecast Tool", func=lambda _: get_demand_forecast(product_id), description="Analyze demand trends"),
        Tool(name="Restock Tool", func=lambda _: restock_tool(product_id, 100), description="Send restock request"),
    ]

    agent = initialize_agent(
        tools=tools,
        llm=ChatOllama(base_url="http://localhost:11434", model="tinyllama"),
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )

    response = agent.run("You are a store manager AI. Analyze current inventory and forecast. Suggest what items to restock and how many.")
    return response
