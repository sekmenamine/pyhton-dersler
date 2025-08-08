import discord
from discord.ext import commands

intents=discord.intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix = "!",intents=intents)

@bot.event
async def on_ready():
    print(f'({bot.user} aktif ve çalışıyor. Bugün çevre için ne yapmak istiyorsun?)')

@bot.command()
async def recycle(ctx,item):
    item=item.lower()
    if item=="pil":
        await ctx.send("piller kesinlikle geri dönüşüm kutularına atılmalı,sakın çevreye atma!")
    elif item=="plastik":
        await ctx.send("plastikler kesinlikle geri dönüşüm kutularına atılmalı,sakın çevreye atma!")
    elif item=="erik çekirdeği":
        await ctx.send("erik çekirdeği organik atıkıtır,kompost yapılabilir")
    else:
        await ctx.send("bu ürün ile ilgili bir bilgim yok,daha sonra güncellenebilir")


@bot.command()
async def tip(ctx):
    await ctx.send("çevre dostu bir hayat için plastik yerine cam kullanın")


@bot.command()
async def helpme(ctx):

    help_text="""  -Geri dönüşüm botu komutları-

    !tip=çevre dostu bilgiler için kullanabilirsiniz
    !helpme= yardım menüsünü gösterir"""

    await ctx.send(help_text)

bot.run("kendi tokeninizi koyun lütfen")