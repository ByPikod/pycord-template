import discord
import os
import sys

from bot import install_logger, PiBot, PiColors
from discord.ext import commands


class OwnerTools(commands.Cog):

    def __init__(self, bot: PiBot):
        self.bot = bot

    ownerGroup = discord.SlashCommandGroup("owner", "Owner commands.")

    @ownerGroup.command(description="Reload extensions attached to the bot.")
    @commands.is_owner()
    async def reload(self, ctx: discord.ApplicationContext):
        self.bot.reload_ext()
        await ctx.respond(
            embed=self.bot.embed(
                title="Yeniden başlatıldı.",
                color=PiColors.GREEN
            )
        )

    @ownerGroup.command(description="Clear the bot console")
    @commands.is_owner()
    async def cls(self, ctx: discord.ApplicationContext):
        os.system("cls")
        await ctx.respond(
            embed=self.bot.embed(
                title="Konsol temizlendi.",
                color=PiColors.GREEN
            )
        )
        print("Konsol temizlendi.")

    @ownerGroup.command(description="Attach latest log file")
    @commands.is_owner()
    async def logs(self, ctx: discord.ApplicationContext):
        filePath = sys.stdout.out_file.name
        print(f"Loglar kaydediliyor: {filePath}")
        sys.stdout.out_file.close()
        install_logger(sys.stdout.stdout)

        await ctx.respond(
            embed=self.bot.embed(
                title="Loglar gönderildi.",
                color=PiColors.GREEN
            ),
            file=discord.File(filePath)
        )

    @ownerGroup.command(description="Make bot say something.")
    @commands.is_owner()
    async def say(self, ctx: discord.ApplicationContext, text: str):
        await ctx.defer(ephemeral=True)
        await ctx.channel.send(content=text)


def setup(bot: PiBot):
    bot.add_cog(OwnerTools(bot))