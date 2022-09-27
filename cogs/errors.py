import traceback

import discord
import discord.ext.commands as commands

from bot import PiBot, PiColors


def setup(bot: PiBot) -> None:

    errors = {
        commands.NoPrivateMessage: {
            "description": "Bu komut özel mesaj yoluyla kullanılamaz.",
            "color": PiColors.RED
        },
        commands.MissingPermissions: {
            "description": "Bu komutu kullanmak için yetkiniz yok.",
            "color": PiColors.RED
        },
        commands.TooManyFlags: {
            "description": "Komut parametrelerini fazla yazdınız :grimacing:",
            "color": PiColors.RED
        },
        commands.MissingRequiredArgument: {
            "description": "Komut parametrelerini eksik yazdınız :grimacing:",
            "color": PiColors.RED
        },
        commands.BadBoolArgument: {
            "description": "Lütfen doğru (true) veya yanlış (false) değer belirtin :grimacing:",
            "color": PiColors.RED
        },
        commands.BadFlagArgument: {
            "description": "Lütfen geçerli bir bayrak belirtin :grimacing:",
            "color": PiColors.RED
        },
        commands.BadColourArgument: {
            "description": "Lütfen geçerli bir renk belirtin :grimacing:",
            "color": PiColors.RED
        },
        commands.BadInviteArgument: {
            "description": "Lütfen geçerli bir davet bağlantısı belirtin :grimacing:",
            "color": PiColors.RED
        },
        commands.MemberNotFound: {
            "description": "Lütfen geçerli bir kişiyi etiketleyerek tekrar deneyin.",
            "color": PiColors.RED
        },
        commands.RoleNotFound: {
            "description": "Lütfen geçerli bir rol etiketleyerek tekrar deneyin.",
            "color": PiColors.RED
        },
        commands.MissingRole: {
            "description": "Bu komutu yalnızca özel bir rol ile kullanabilirsiniz.",
            "color": PiColors.RED
        },
        commands.BotMissingPermissions: {
            "description": "Bu komutu yürütmek için yetkim yok.",
            "color": PiColors.RED
        },
        commands.CommandInvokeError: {
            "description": "Komut yürütülürken bir hata oluştu. Komutu yürütmeye yetkim olmayabilir.",
            "color": PiColors.RED
        },
        commands.ChannelNotFound: {
            "description": "Lütfen geçerli bir kanal etiketleyerek tekrar deneyin.",
            "color": PiColors.RED
        }
    }

    @bot.listen()
    async def on_command_error(ctx: commands.Context, error: commands.CommandError):

        if isinstance(error, commands.CommandNotFound):
            return

        if type(error) in errors:
            await ctx.reply(embed=bot.embed(**errors[error]))
            return

        traceback.print_exception(error)

    @bot.listen()
    async def on_application_command_error(ctx: discord.ApplicationContext, error: commands.CommandError):

        if isinstance(error, commands.CommandNotFound):
            return

        if type(error) in errors:
            await ctx.reply(embed=bot.embed(**errors[error]))
            return

        traceback.print_exception(error)
