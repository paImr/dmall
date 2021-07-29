import discord
client = discord.Client()
@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(f'{user.mention}, discord.gg/eboys made by static#0006')
    except:
        print(f"couldnt message: {user.name}")
client.run("TOKEN GOES HERE", bot=False)
