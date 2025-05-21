import discord
from discord.ext import commands

intens=discord.intensts.default()
intens.message_content=True

bot=commands.Bot(command_prefix="!", intens=intens)

@bot.event
async def on_ready():
    print(f'({bot.user} aktif ve çalışıyor. Buün çevre için ne yapmak istiyorsunuz?)')

@bot.command()
async def recycle(ctx,items):
    items=items.lower()
    if items=="pil":
        await ctx.send("piller kesinlikle geri dönüşüm kutularına atılmalı,sakın çevreye atma!")    
    elif items=="plastik":
        await ctx.send("plastikler kesinlikle geri dönüşüm kutularına atılmalı,sakın çevreye atma!")    
    elif items=="erik çekirdeği":
        await ctx.send("erik çekirdeği organik istediğin gibi at") 
    else:
        await ctx.send("bu ürünü bilmiyorum")      






