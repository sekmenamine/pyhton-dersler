import discord

intents = discord.Intents.default()
intents.message_content=True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptı.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("merhaba"):
        await message.channel.send("Selam!")
    elif message.content.startswith("bye"):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("selamun aleyküm tostum"):
        await message.channel.send("Aleyküm Selam Tostummmmmm!!!🤲🤝")
    else:
        await message.channel.send(message.content)

client.run("--token--")            