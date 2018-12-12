# Work with Python 3.6
import discord
import config as cfg

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    message.content = message.content.lower()
    if message.content.find('happy birthday') >= 0:
        msg = 'Merci ;) {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(cfg.TOKEN)