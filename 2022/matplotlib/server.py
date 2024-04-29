import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print(f"Received {message}")

async def main():
    async with serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())

