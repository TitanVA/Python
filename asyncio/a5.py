import asyncio
import random


async def f():
    while True:
        print("f function")
        await asyncio.sleep(1)


async def g_helper():
    print("g_helper")
    return random.randint(0, 100)


async def g():
    while True:
        print(await g_helper())
        print("g function")
        await asyncio.sleep(1)


async def main():
    main_loop.create_task(g())
    main_loop.create_task(f())


main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())
main_loop.run_forever()
