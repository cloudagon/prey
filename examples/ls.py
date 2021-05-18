#!/usr/bin/env prey


async def main():
    await x("ls -a")
    cd("..")
    a = await x("ls")
    await asyncio.sleep(2)
