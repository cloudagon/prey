#!/usr/bin/env prey


async def main():
    await _("cat pyproject.toml | grep name")

    branch = await _("git branch --show-current")
    await _(f"dep deploy --branch={branch}")

    await _(
        [
            "sleep 1; echo 1",
            "sleep 2; echo 2",
            "sleep 3; echo 3",
        ]
    )

    name = "foo"
    await _(f"mkdir /tmp/{name}")
