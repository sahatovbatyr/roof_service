import asyncio
from asyncio import sleep

async def make_request(count):
    print("making DB request", count)
    await sleep(0.1)



async def main():
    chunk = 200
    tasks = []
    pending = 0

    for i in range(10_000):
        tasks.append( asyncio.create_task( make_request(i) ) )
        pending+=1

        if len(tasks) == chunk or pending == 10_000:
            await asyncio.gather(*tasks)
            tasks = []

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

