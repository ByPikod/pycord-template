import sys

import discord

from bot import install_logger, PiBot


if __name__ == "__main__":

    install_logger(sys.stdout)
    myIntents = discord.Intents.all()
    client = PiBot(owner=449188680079507476, intents=myIntents, debug_guilds=[748913297042046997])
    client.run("Njg4MzcwMDkzNTk5NjIxMjYw.G_3qjW.c6dhI1f3ao6z_pn7JCj5S7mQgYwWMjRK033ODI")