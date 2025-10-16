import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
from dedalus_labs.utils.streaming import stream_async

load_dotenv()

async def main():
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = runner.run(
        input="Roll a die two times, multiply the results, and return the final result. Show your working.",
        model="openai/gpt-5-mini",
        mcp_servers=["itsmcollins/dedalus-dice-roller"],
        stream=True
    )

    await stream_async(result)

if __name__ == "__main__":
    asyncio.run(main())