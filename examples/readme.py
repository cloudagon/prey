#!/usr/bin/env prey


async def main():
    await x("cat pyproject.toml | grep name")

    branch = await x("git branch --show-current")
    await x(f"dep deploy --branch={branch}")

    await x(
        [
            "sleep 1; echo 1",
            "sleep 2; echo 2",
            "sleep 3; echo 3",
        ]
    )

    name = "foo"
    await x(f"mkdir /tmp/{name}")
