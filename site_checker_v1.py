import aiohttp
import asyncio


class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()


async def check(url):
    async with AsyncSession(url) as response:
        print(f'{url}: status -> {response.status}')
        html = await response.text()
        print(f'{url}: type -> {html[:15].strip()}')


async def main():
    await asyncio.gather(
        check('https://google.com'),
        check('https://onliner.by'),
    )

asyncio.run(main())
