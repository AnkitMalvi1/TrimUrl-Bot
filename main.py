import os
import random
import discord
import requests
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(1060250117736767508)
    await channel.send(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


def link_short(user_url):
    url = "https://url-shortener-service.p.rapidapi.com/shorten"

    payload = {
        'url': user_url}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "YOUR API KEY",
        "X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    RES = response.json()

    return RES['result_url']


@client.event
async def on_message(message):
    # If the message was sent by the bot itself, return
    if message.author == client.user:
        return

    if message.content.startswith("$short"):
        user_url = message.content[7:]
        result_url = link_short(user_url)
        color = random.randint(0, 16777215)
        embed = discord.Embed(
            title="SHORT URL", description=result_url, color=color)
        embed.set_thumbnail(
            url="https://rapidapi.com/cdn/images?url=https://rapidapi-prod-apis.s3.amazonaws.com/66/c6a88185b34a1faa638a15c40d502f/67a6c8317e554351331be84f2f1933b3.png")

        embed.set_footer(text="Made with love by Ankit.")
        await message.channel.send(embed=embed)


client.run('YOUR BOT TOKEN')
