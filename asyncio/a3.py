import asyncio


async def count(counter):
    print(f"Number of items in list: {len(counter)}")

    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)


async def print_every_one_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f"- 1 sec gone. Count of items in list: {len(counter)}")


async def print_every_5_sec(counter):
    while True:
        await asyncio.sleep(5)
        print(f"----- 5 sec gone. Count of items in list: {len(counter)}")


async def print_every_10_sec(counter):
    while True:
        await asyncio.sleep(10)
        print(f"---------- 10 sec gone. Count of items in list: {len(counter)}")


async def main():
    counter = list()

    tasks = [
        count(counter), print_every_one_sec(counter), print_every_5_sec(counter), print_every_10_sec(counter)
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
