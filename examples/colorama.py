#!/usr/bin/env prey


async def main():
    await _(
        [
            # be sure to reset styles or everything after it will still be styled
            f"echo {colorama.Fore.RED} this is red{colorama.Style.RESET_ALL}",
            f"echo this is normal",
            f'echo {colorama.Back.LIGHTBLACK_EX}{colorama.Fore.YELLOW}this has a "light black" background and yellow text{colorama.Style.RESET_ALL}',
        ]
    )
