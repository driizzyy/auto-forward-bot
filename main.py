import json
import discord
import asyncio

with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['token']
SOURCE_CHANNEL_ID = int(config['source_channel_id'])
DESTINATION_CHANNEL_ID = int(config['destination_channel_id'])
FORWARD_SELF_MESSAGES = config.get('forward_self_messages')

client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
@client.event
async def on_message(message):
    if message.channel.id != SOURCE_CHANNEL_ID:
        return
    if not FORWARD_SELF_MESSAGES and message.author.id == client.user.id:
        return
    destination = client.get_channel(DESTINATION_CHANNEL_ID)
    if destination is None:
        print(f"Destination channel not found: {DESTINATION_CHANNEL_ID}")
        return
    try:
        await destination.send(message.content)
        print(f"Forwarded: {message.content}")
    except Exception as e:
        print(f"Failed to forward message: {e}")

client.run(TOKEN)