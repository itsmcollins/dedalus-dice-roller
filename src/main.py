# src/main.py
from fastmcp import FastMCP
import random

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_die() -> int:
    return random.randint(1, 6)

@mcp.tool
def multiply(a: int, b: int) -> int:
    return a * b

def main():
    # Dedalus requires streamable HTTP for remote servers
    mcp.run(transport="streamable-http")