import discord
import asyncio
import datetime
import os
import subprocess
import combine2

'''
1. Use dc lib to dload vids
2. filter out all other content
3. specify date and time frame
4. wtf is intents
5. mayb place in sep folders? (future)
'''
#part1
#intents and tokens
TOKEN = ' *** '
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#part2
#downloading the shi
async def download_videos(start_time, end_time):
    guild = discord.utils.get(client.guilds, name='EchiRoomPro')
    channel = discord.utils.get(guild.channels, name='test')

    async for message in channel.history(limit=None, after=start_time, before=end_time):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type.startswith('video'):
                    await attachment.save(attachment.filename)
                    print('Downloaded video: {}'.format(attachment.filename))

#part3
#driver fn.
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    start_time = datetime.datetime(2023, 4, 26, 0, 0, 0)
    end_time = datetime.datetime(2023, 4, 27, 0, 0, 0)
    await download_videos(start_time, end_time)
    combine2.combine_videos()

client.run(TOKEN)

