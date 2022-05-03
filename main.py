import asyncio
import os
import pathlib
import logging
from decimal import Decimal, localcontext
from contextlib import contextmanager
from time import time

import aiohttp
import pytest


file_path = pathlib.Path('hello.txt')

try:
    with file_path.open(mode='w') as file:
        file.write('Hello, World!')
except OSError as error:
    logging.error(f'Writing to file {file_path} failed due to: {error}')


with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name, '->', entry.stat().st_size, 'bytes')


with localcontext() as ctx:
    ctx.prec = 21
    print(Decimal('1') / Decimal('42'))


with pytest.raises(ZeroDivisionError) as exc:
    1 / 0

assert str(exc.value) == 'division by zero'

favorites = {'fruit': 'apple', 'pet': 'dog'}

with pytest.raises(KeyError) as exc:
    favorites['car']


async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'{url}: status -> {response.status}')
            html = await response.text()
            print(f'{url}: type -> {html[:17].strip()}')


async def main():
    await asyncio.gather(
        check('https://realpython.com'),
        check('https://pycoders.com'),
    )

asyncio.run(main())


@contextmanager
def hello_context_manager():
    print('Rntering the context...')
    yield 'Hello!'
    print('Leaving the context')


with hello_context_manager() as hello:
    print(hello)


@contextmanager
def writable_file(file_path):
    file = open(file_path, mode='w')
    try:
        yield file
    finally:
        file.close()


with writable_file('hello.txt') as file:
    file.write('Hello write!')


@contextmanager
def mock_time():
    global time
    saved_time = time
    time = lambda: 42
    yield
    time = saved_time


with mock_time():
    print(f'Mocked time: {time()}')

print(time())
