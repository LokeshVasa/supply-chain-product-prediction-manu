from mcp.server import FastMCP  # Correct import path
from server.predict_impl import predict_product_weight

mcp = FastMCP("predict_demand")

@mcp.tool()
async def get_product_weight() -> str:
    """Predict the product weight in tons"""
    try:
        weight = predict_product_weight()
        return f"Predicted weight in tons: {weight}"
    except Exception as e:
        return f"Error predicting weight: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")