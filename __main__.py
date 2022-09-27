import sys

import discord

from bot import install_logger, PiBot


if __name__ == "__main__":

    install_logger(sys.stdout)
    myIntents = discord.Intents.all()
    client = PiBot(owner=449188680079507476, intents=myIntents, debug_guilds=[748913297042046997])
    client.run("Njg4MzcwMDkzNTk5NjIxMjYw.GlDW-6.lixJWf7Lu6Dk-E_hPbcL7coL6M6138gTa7L9b0")