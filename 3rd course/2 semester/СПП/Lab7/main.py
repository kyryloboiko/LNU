import csv
import time
import asyncio
import aiofiles
import reactivex as rx
from reactivex import operators as ops


def default_func():
    with open(r'E:\СПП\Lab7\csv2.csv', 'r', encoding='utf8') as file:
        start = time.time()
        print('--- default ---')

        reader = csv.DictReader(file)
        count = sum(1 for row in reader if row['country'] == 'Ukraine')

        print(f'Ukraine count: {count}')
        print(f'Time: {round(time.time() - start, 4)} sec')


async def async_func():
    async with aiofiles.open(r'E:\СПП\Lab7\csv2.csv', 'r', encoding='utf8') as file:
        start = time.time()
        print('--- async ---')

        lines = await file.readlines()
        header = lines[0].strip().split(',')
        country_index = header.index('country')

        count = sum(1 for line in lines[1:] if line.strip().split(',')[country_index] == 'Ukraine')

        print(f'Ukraine count: {count}')
        print(f'Time: {round(time.time() - start, 4)} sec')


async def rx_func():
    async with aiofiles.open(r'E:\СПП\Lab7\csv2.csv', 'r', encoding='utf8') as file:
        start = time.time()
        print('--- rx ---')

        lines = await file.readlines()
        header = lines[0].strip().split(',')
        country_index = header.index('country')
        data = lines[1:]

        rx.from_(data).pipe(
            ops.map(lambda line: line.strip().split(',')),
            ops.filter(lambda parts: len(parts) > country_index and parts[country_index] == 'Ukraine'),
            ops.count()
        ).subscribe(lambda count: print(f'Ukraine count: {count}'))

        print(f'Time: {round(time.time() - start, 4)} sec')


# Запуск
default_func()
print()
asyncio.run(async_func())
print()
asyncio.run(rx_func())
