#!/usr/bin/env prey


async def main():
    count = int(await x("ls -1 | wc -l"))
    print(f"Files count: {count}")
