import nextcord
from nextcord.ext import commands
from firebase import get_user_data, update_user_data, get_all_users_data

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_interaction(self, interaction: nextcord.Interaction):
        if interaction.type == nextcord.InteractionType.application_command:
            user_id = str(interaction.user.id)
            user_data = get_user_data(user_id)

            if user_data:
                user_data['exp'] += 1
                if user_data['exp'] >= user_data['level'] * 15:
                    user_data['level'] += 1
                    await interaction.channel.send(f"{interaction.user.mention} has leveled up to level {user_data['level']}!")
            else:
                user_data = {'exp': 1, 'level': 1}

            update_user_data(user_id, user_data)

    @nextcord.slash_command(name="level", description="Check your current level and experience.")
    async def level(self, interaction: nextcord.Interaction):
        user_id = str(interaction.user.id)
        user_data = get_user_data(user_id)

        if user_data:
            embed = nextcord.Embed(title=f"{interaction.user.name}'s Level", color=nextcord.Color.blue())
            embed.add_field(name="Level", value=user_data['level'])
            embed.add_field(name="Exp", value=user_data['exp'])
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("You haven't sent any commands yet!")

    @nextcord.slash_command(name="leaderboard", description="View the top 10 users by XP.")
    async def leaderboard(self, interaction: nextcord.Interaction):
        await interaction.response.defer()
        all_users_data = get_all_users_data()
        if all_users_data:
            sorted_users = sorted(all_users_data.items(), key=lambda item: item[1]['exp'], reverse=True)
            
            embed = nextcord.Embed(title="Leaderboard", color=nextcord.Color.gold())
            
            for i, (user_id, user_data) in enumerate(sorted_users[:10]):
                try:
                    user = await self.bot.fetch_user(int(user_id))
                    embed.add_field(name=f"{i+1}. {user.name}", value=f"Level: {user_data['level']} | XP: {user_data['exp']}", inline=False)
                except nextcord.NotFound:
                    embed.add_field(name=f"{i+1}. Unknown User", value=f"Level: {user_data['level']} | XP: {user_data['exp']}", inline=False)

            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send("No users found in the leaderboard.")

def setup(bot):
    bot.add_cog(Leveling(bot))