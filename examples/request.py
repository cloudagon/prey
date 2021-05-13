#!/usr/bin/env prey


async def main():
    response = await request("get", "http://python.org")

    print("Status:", response.status)
    print("Content-type:", response.headers["content-type"])

    html = await response.text()
    print("Body:", html[:15], "...")
