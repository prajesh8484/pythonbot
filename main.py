import nextcord
from nextcord.ext import commands
import requests
import json
import datetime
import asyncio
import pytz
import random



intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description="My Bot", intents=intents)



@bot.event
async def on_ready():
     print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.slash_command(description="a slash command")
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")  # .send = reply  || .send_message = send message


@bot.slash_command(description="bow")
async def dog(interaction: nextcord.Interaction):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await interaction.response.send_message(image_link)

@bot.slash_command(description="sends a message to this channel")
async def send(interaction: nextcord.Interaction, text: str):
    await interaction.response.send_message(f"{text}")

@bot.slash_command(description="get current time")
async def timenow(interaction: nextcord.Interaction):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ist = pytz.timezone('YOUR_TIME_ZONE')  #e.g. America/New_York
    datetime_ist = datetime.datetime.now(ist)
    current_time = datetime_ist.strftime("%H:%M:%S")
    await interaction.response.send_message(f"Current Time is {current_time}")


@bot.slash_command(description="pong")
async def ping(interaction: nextcord.Interaction):
    apipng = random.randint(70, 148)
    databasepng = random.randint(100, 130)
    await interaction.response.send_message(f"Pong! :ping_pong:\nAPI Ping: `{apipng}ms`\nDatabase Ping: `{databasepng}ms`")

@bot.command()
async def sendtochannel(ctx, text: str):
    channel = bot.get_channel(YOUR_CHANNEL_ID)
    await channel.send(text)

@bot.command()
async def slap(ctx, members: commands.Greedy[nextcord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')

@bot.slash_command(description="alright im here to help")
async def help(interaction: nextcord.Interaction):
    await interaction.response.send_message("**Hello I'm David Bot**\n*My commands are as follows:*\n\n`!slap !sendtochannel !codelink`\n\n*And some slash commands ;)*")


async def schedule_daily_message():
    while True:     
        now =  datetime.datetime.now()
        then = now+datetime.timedelta(days-1) 
        then.replace(hour-8, minute-0) 
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)

        channel = bot.get_channel(YOUR_CHANNEL_ID)

        await channel.send("Good Morning")


bot.run("YOUR_BOT_TOKEN")
