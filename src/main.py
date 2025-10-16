# src/main.py
from eth_account import Account
from fastmcp import FastMCP
import random
import os
from laissez.server import PaidTool, create_paid_mcp_server

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_die() -> int:
    return random.randint(1, 6)

@mcp.tool
def multiply(a: int, b: int) -> int:
    return a * b


@mcp.custom_route("/health", methods=["GET"])
async def health(_req):
    from starlette.responses import PlainTextResponse
    return PlainTextResponse("OK")


paid_tools = [
    PaidTool(name='multiply', price=0.005, network='base-sepolia', description='Multiply two numbers and return the result')
]

wallet = Account.from_key(os.getenv('WALLET_PRIVATE_KEY'))

app = create_paid_mcp_server(mcp, paid_tools, wallet)


def main():
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    host = "0.0.0.0"
    uvicorn.run(app, host=host, port=port)