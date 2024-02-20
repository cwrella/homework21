import asyncio
import time
import requests
async def load():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    s = response.status_code
    print(s)
    await asyncio.sleep(1)

async def main():
    tasks = [load() for i in range(100)]
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
print(time.time() - start)
