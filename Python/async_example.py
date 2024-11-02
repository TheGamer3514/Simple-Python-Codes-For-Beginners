"""
async_example.py
This script demonstrates a basic asynchronous function using asyncio.
"""

import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(greet())
