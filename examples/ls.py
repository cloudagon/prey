#!/usr/bin/env prey


async def main():
    await _("ls -a")
    cd("..")
    a = await _("ls")
    await asyncio.sleep(2)
