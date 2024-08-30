from PythonClient import CServer
import asyncio
import time

# CSserver.debug(True)
def run(data):
    print(data)
    return {"hello": "world"}
async def main():
    client = CServer('127.0.0.1',9800)
    await client.connect()
    if await client.register("program908"):
        print("SUCCEFUL")
    
    for i in range(10000):
        __ = time.time()
        await client.functionCall("program_iomm@run","{'hello':'1'}")
        print(time.time() - __)

asyncio.run(main())
