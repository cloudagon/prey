#!/usr/bin/env prey


async def main():
    count = int(await _("ls -1 | wc -l"))
    print(f"Files count: {count}")
