import discord
import os
from datetime import datetime

from discord.ext import commands
from bot.colors import PiColors


class PiBot(discord.Bot):

    owner_ids = []
    owners = []
    exts = []

    async def on_ready(self) -> None:

        print("Fetching owners...")
        self.owners = []
        users = [await self.fetch_user(owner_id) for owner_id in self.owner_ids]
        self.owners += users
        owner_text = self.get_owners_text()

        print(f"Owners: {owner_text}")
        print(f"Logged as {self.user}")

    def __init__(self, owner: int | tuple = tuple(), *args, **kwargs):

        super(PiBot, self).__init__(*args, **kwargs)

        if not os.path.exists("cogs"):
            os.mkdir("cogs")

        if not isinstance(owner, tuple):
            self.owner_ids = (owner,)
        else:
            self.owner_ids = owner

        self.load_ext()

    def load_ext(self):

        self.exts = self.load_extensions("cogs", recursive=True, store=True)

        for k in self.exts:

            v = self.exts[k]

            if v is True:
                print(f"Loaded successfully: {k}")
                continue

            print(v)

    def reload_ext(self):

        print("Reloading...")
        for k in self.exts:
            self.unload_extension(k)
            print(f"Unloaded extension: {k}")

        print("Starting to reload extensions.")
        self.load_ext()

    def get_owners_text(self) -> str:
        return ', '.join(str(owner) for owner in self.owners)

    def embed(self, **kwargs) -> discord.Embed:

        color = kwargs.get("color")
        embed = kwargs.get("embed")

        if color is not None:
            kwargs.__setitem__("color", color.value)
        else:
            kwargs.__setitem__("color", PiColors.BLUE.value)

        if embed is None:
            created_embed = discord.Embed(**kwargs)
        else:
            created_embed = embed

        created_embed.timestamp = datetime.now()
        created_embed.set_footer(text="Powered by " + self.get_owners_text(), icon_url=self.owners[0].avatar.url)

        return created_embed

    async def is_owner(self, user: discord.User) -> bool:
        return user in self.owners
