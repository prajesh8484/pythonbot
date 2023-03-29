import nextcord
from nextcord.ext import commands
import requests
import json
import datetime
import asyncio
import pytz
import random
import time



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
async def ping(ctx):
    start_time = time.monotonic()
    message = await ctx.send("Pong!")
    end_time = time.monotonic()
    await message.edit(content=f"Pong! Response time: {round((end_time - start_time) * 1000)} ms")
     

@bot.slash_command(description="rolle's dice")
async def rolldice(interaction: nextcord.Interaction):
    rolled = random.randint(1, 6)
    await interaction.send(f"*clatter* you rolled dice and you got {rolled}!") 

@bot.slash_command(description="ban a user")
async def ban(ctx: commands.Context, user: nextcord.Member, reason: str="No reason provided"):
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"{user} has been banned from the server! Reason: {reason}!")  

@bot.slash_command(description="kick a user")
async def kick(ctx: commands.Context, user: nextcord.Member, reason: str="No reason provided"):
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} has been kicked from the server! Reason: {reason}!") 

     
@bot.slash_command(description="Retrieves the avatar of a user.")
async def avatar(ctx, user: nextcord.Member = None):
    user = user or ctx.author
    avatar_url = user.avatar.url
    await ctx.send(avatar_url)


     
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

@bot.slash_command(name="userinfo", description="Get detailed information about a user.")
async def userinfo(ctx: nextcord.InteractionType, user: nextcord.Member = None):
    if user is None:
        user = ctx.user
    
    # Get information about the user
    username = str(user)
    created_at = user.created_at.strftime("%Y-%m-%d \n*%H:%M:%S* UTC")
    joined_at = user.joined_at.strftime("%Y-%m-%d \n*%H:%M:%S* UTC")
    roles = [role.mention for role in user.roles if role != ctx.guild.default_role]
    if len(roles) == 0:
        roles = ["None"]
    user_id = str(user.id)
    avatar_url = user.avatar.url
    

    embed = nextcord.Embed(title="User Information", color=0x00ff00)
    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name="Username", value=username, inline=False)
    embed.add_field(name="Account Created On", value=created_at, inline=False)
    embed.add_field(name="Joined This Server On", value=joined_at, inline=False)
    embed.add_field(name="Roles", value=", ".join(roles), inline=False)
    embed.add_field(name="Status", value=user.status, inline=False)
    embed.add_field(name="User ID", value=user_id, inline=False)
    embed.add_field(name="Activity", value=user.activity, inline=False)
    await ctx.send(embed=embed)

          
bot.run("YOUR_BOT_TOKEN")
