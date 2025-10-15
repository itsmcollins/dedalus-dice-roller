# src/main.py
from fastmcp import FastMCP
import random
import os

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

def main():
    port = int(os.getenv("PORT", 8080))
    host = "0.0.0.0"
    mcp.run(transport="streamable-http", host=host, port=port)