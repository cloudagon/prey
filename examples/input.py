#!/usr/bin/env prey


async def main():
    word = input("Give me a word: ")
    await _(f"echo {word}")
