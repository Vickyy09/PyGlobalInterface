from PythonClient import CServer
import asyncio


def run(data):
    print(data)
    return {"hello": "world"}
async def main():
    client = CServer('127.0.0.1',9800)
    await client.connect()
    if await client.register("program_iomm"):
        print("SUCCEFUL")
    
    if await client.register_function("run",run):
        print("run function")
    await client.run_forver()

asyncio.run(main())
