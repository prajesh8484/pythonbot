import nextcord
from nextcord.ext import commands
import aiohttp
import datetime
import pytz
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description="My Bot", intents=intents)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    else:
        await ctx.send(f"An error occurred: {error}")

@bot.event
async def on_ready():
     print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.slash_command(description="a slash command")
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")  # .send = reply  || .send_message = send message


@bot.slash_command(description="bow")
async def dog(interaction: nextcord.Interaction):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as response:
            if response.status == 200:
                data = await response.json()
                await interaction.response.send_message(data['message'])
            else:
                await interaction.response.send_message("Could not fetch a dog image.")

@bot.slash_command(description="meow")
async def cat(ctx: nextcord.Interaction):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.thecatapi.com/v1/images/search") as response:
            if response.status == 200:
                data = await response.json()
                await ctx.send(data[0]['url'])
            else:
                await ctx.send("Could not fetch a cat image.")

@bot.slash_command(description="sends a message to this channel")
async def send(interaction: nextcord.Interaction, text: str):
    await interaction.response.send_message(f"{text}")

@bot.slash_command(name="nickname", description="Change your nickname in the server")
async def nickname(ctx: nextcord.Interaction, nickname: str):
    try:
        await ctx.user.edit(nick=nickname)
        await ctx.send(f"Your nickname has been changed to {nickname}")
    except nextcord.errors.Forbidden:
        await ctx.send("I don't have permission to change your nickname.")

@bot.slash_command(description="get current time")
async def timenow(interaction: nextcord.Interaction):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    ist = pytz.timezone('Asia/Kolkata') 
    datetime_ist = datetime.datetime.now(ist)
    current_time = datetime_ist.strftime("%H:%M:%S")
    await interaction.response.send_message(f"Current Time is {current_time}")


@bot.slash_command(description="pong")
async def ping(ctx: nextcord.Interaction):
    start_time = time.monotonic()
    message = await ctx.send("Pinging...")
    end_time = time.monotonic()
    
    latency = bot.latency * 1000  
    response_time = (end_time - start_time) * 1000  
    
    embed = nextcord.Embed(title="Pong!", color=nextcord.Color.green())
    embed.add_field(name="Websocket Latency", value=f"{latency:.2f} ms", inline=False)
    embed.add_field(name="Response Time", value=f"{response_time:.2f} ms", inline=False)
    
    await message.edit(content=None, embed=embed)
     

@bot.slash_command(description="Rolls a standard six-sided die.")
async def rolldice(interaction: nextcord.Interaction):
    """Rolls a die and shows the result with ASCII art."""
    roll = random.randint(1, 6)
    dice_art = {
        1: "```\n+-------+\n|       |\n|   o   |\n|       |\n+-------+\n```",
        2: "```\n+-------+\n| o     |\n|       |\n|     o |\n+-------+\n```",
        3: "```\n+-------+\n| o     |\n|   o   |\n|     o |\n+-------+\n```",
        4: "```\n+-------+\n| o   o |\n|       |\n| o   o |\n+-------+\n```",
        5: "```\n+-------+\n| o   o |\n|   o   |\n| o   o |\n+-------+\n```",
        6: "```\n+-------+\n| o   o |\n| o   o |\n| o   o |\n+-------+\n```"
    }
    embed = nextcord.Embed(
        title="Dice Roll",
        description=f"🎲 You rolled a **{roll}**!",
        color=nextcord.Color.from_rgb(255, 255, 255)
    )
    embed.add_field(name="Result", value=dice_art[roll], inline=False)
    await interaction.send(embed=embed)

@bot.slash_command(description="Tosses a coin and displays the result with ASCII art.")
async def cointoss(interaction: nextcord.Interaction):
    import random

    outcome = random.choice(["Heads", "Tails"])
    coin_art = {
        "Heads": (
            "```\n"
            "+------+\n"
            "|      |\n"
            "|   H  |\n"
            "|      |\n"
            "+------+\n"
            "```"
        ),
        "Tails": (
            "```\n"
            "+------+\n"
            "|      |\n"
            "|   T  |\n"
            "|      |\n"
            "+------+\n"
            "```"
        )
    }
    embed = nextcord.Embed(
        title="🪙 Coin Toss Result",
        description=f"🎲 The coin landed on **{outcome}**!",
        color=nextcord.Color.gold()
    )
    embed.add_field(name="Visual", value=coin_art[outcome], inline=False)
    embed.set_footer(text="Use /cointoss again to try your luck!")
    await interaction.send(embed=embed)


@bot.slash_command(description="ban a user")
async def ban(ctx: nextcord.Interaction, user: nextcord.Member, reason: str="No reason provided"):
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"{user} has been banned from the server! Reason: {reason}!")  

@bot.slash_command(description="kick a user")
async def kick(ctx: nextcord.Interaction, user: nextcord.Member, reason: str="No reason provided"):
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} has been kicked from the server! Reason: {reason}!") 

     
@bot.slash_command(description="Retrieves the avatar of a user.")
async def avatar(ctx, user: nextcord.Member = None):
    user = user or ctx.user
    avatar_url = user.avatar.url
    await ctx.send(avatar_url)
     
async def sendtochannel(ctx, channel: nextcord.TextChannel, text: str):
    await channel.send(text)

@bot.command()
async def slap(ctx, members: commands.Greedy[nextcord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')

@bot.slash_command(description="alright im here to help")
async def help(interaction: nextcord.Interaction):
    await interaction.response.send_message(f"**Hello I'm {bot.user}**\n*My commands are as follows:*\n\n`!slap !sendtochannel !codelink`\n\n*And some slash commands ;)*")


@bot.slash_command(description="Ask a question to 8 ball")
async def eightball(ctx, question: str):
    responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "Outlook not so good.", "My sources say no.", "Very doubtful."]
    await ctx.send(random.choice(responses))

@bot.slash_command(name="userinfo", description="Get detailed information about a user.")
async def userinfo(ctx: nextcord.Interaction, user: nextcord.Member = None):
    if user is None:
        user = ctx.user
    
    username = str(user)
    created_at = user.created_at.strftime("%Y-%m-%d \n*%H:%M:%S*  UTC")
    joined_at = user.joined_at.strftime("%Y-%m-%d \n*%H:%M:%S*  UTC")
    roles = [role.mention for role in user.roles if role != ctx.guild.default_role]
    if len(roles) == 0:
        roles = ["None"]
    user_id = str(user.id)
    avatar_url = user.avatar.url
    activity = str(user.activity) if user.activity else "None"

    embed = nextcord.Embed(title="User Information", color=0x00ff00)
    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name="Username", value=username, inline=False)
    embed.add_field(name="Account Created On", value=created_at, inline=False)
    embed.add_field(name="Joined This Server On", value=joined_at, inline=False)
    embed.add_field(name="Roles", value=", ".join(roles), inline=False)
    embed.add_field(name="Status", value=user.status, inline=False)
    embed.add_field(name="User ID", value=user_id, inline=False)
    embed.add_field(name="Activity", value=activity, inline=False)
    await ctx.send(embed=embed)

@bot.slash_command()
async def mute(ctx: nextcord.Interaction, user: nextcord.Member):
    if ctx.user.guild_permissions.administrator: 
        try:             
            await user.edit(mute=True)
        except:
            await ctx.send("user is not connected to any voice channel.")
        else:           
            await ctx.send(f"{user.display_name} has been muted.")
    else:
        await ctx.send("You do not have permission to use this command.")

          
@bot.slash_command()
async def unmute(ctx: nextcord.Interaction, user: nextcord.Member):
    if ctx.user.guild_permissions.administrator: 
        try:             
            await user.edit(mute=False)
        except:
            await ctx.send("user is not connected to any voice channel.")
        else:           
            await ctx.send(f"{user.display_name} has been unmuted.")
    else:
        await ctx.send("You do not have permission to use this command.")


@bot.slash_command(name="announce",description="Announce a message in a specific channel")
async def announce(ctx: nextcord.Interaction, channel: nextcord.TextChannel, message: str):
    if ctx.user.guild_permissions.administrator:
        await channel.send(f":loudspeaker: Announcement : \n@everyone {message}")
    else:
        await ctx.send("You don't have the necessary permissions to use this command.")

          
          
bot.run(os.getenv("BOT_TOKEN"))