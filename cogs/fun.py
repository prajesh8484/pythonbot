import nextcord
from nextcord.ext import commands
import aiohttp

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = None

    async def _get_session(self):
        if self.session is None:
            self.session = aiohttp.ClientSession()
        return self.session

    def cog_unload(self):
        if self.session:
            self.bot.loop.create_task(self.session.close())

    @nextcord.slash_command(name="meme", description="Get a random meme")
    async def meme(self, interaction: nextcord.Interaction):
        session = await self._get_session()
        await interaction.response.defer()
        async with session.get("https://meme-api.com/gimme") as response:
            if response.status == 200:
                data = await response.json()
                embed = nextcord.Embed(title=data['title'], url=data['postLink'], color=nextcord.Color.random())
                embed.set_image(url=data['url'])
                embed.set_footer(text=f"r/{data['subreddit']} | {data['ups']} upvotes")
                await interaction.followup.send(embed=embed)
            else:
                await interaction.followup.send("Could not fetch a meme.")

    @nextcord.slash_command(name="quote", description="Get an aesthetic quote")
    async def quote(self, interaction: nextcord.Interaction):
        session = await self._get_session()
        await interaction.response.defer()
        async with session.get("http://api.quotable.io/random") as response:
            if response.status == 200:
                data = await response.json()
                embed = nextcord.Embed(title="Quote", description=f"\"{data['content']}\"", color=nextcord.Color.blurple())
                embed.set_footer(text=f"- {data['author']}")
                await interaction.followup.send(embed=embed)
            else:
                await interaction.followup.send("Could not fetch a quote.")

    @nextcord.slash_command(name="waifu", description="Get a random waifu image")
    async def waifu(self, interaction: nextcord.Interaction):
        session = await self._get_session()
        await interaction.response.defer()
        async with session.get("https://api.waifu.pics/sfw/waifu") as response:
            if response.status == 200:
                data = await response.json()
                embed = nextcord.Embed(title="Waifu", color=0xFFC0CB)
                embed.set_image(url=data['url'])
                await interaction.followup.send(embed=embed)
            else:
                await interaction.followup.send("Could not fetch a waifu.")

def setup(bot):
    bot.add_cog(Fun(bot))
