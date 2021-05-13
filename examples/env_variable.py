#!/usr/bin/env prey


async def main():
    import os

    os.environ["FOO"] = "bar"
    await _("echo $FOO")
