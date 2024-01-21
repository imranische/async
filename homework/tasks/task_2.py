import asyncio


async def magic_func() -> int:
    return 42


async def fix_this_code() -> int:
    # С этой функцией что-то не так, необходимо разобраться что именно и починить её.
    # FIX THIS CODE
    y = asyncio.create_task(magic_func())
    await y
    return y

if __name__ == '__main__':
    print(asyncio.run(fix_this_code()))
