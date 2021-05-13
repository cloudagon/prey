#!/usr/bin/env prey


async def main():
    await _("curl https://cdn.jsdelivr.net/npm/jquery@3.2.1/dist/jquery.min.js")
    cd("..")
    print(await _("ls"))
