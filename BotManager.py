import configs.DefaultConfig as defaultConfig
import utils.DiscordUtil as discordUtil

import asyncio, os
import discord
from discord.ext import commands
from cogs.GeminiCog import GeminiAgent


intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!",intents=intents,help_command=None)

@bot.event
async def on_ready():
    print("Bot is online..")

@bot.event
async def on_member_join(member):
    print("New member is joining")
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}! Feel free to ask me questions here.")

@bot.command(aliases = ["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title = "UPDATE V10",
                            description = "CHAT BOT AI",
                            color = discord.Color.dark_purple())
    MyEmbed.set_thumbnail(url = "https://th.bing.com/th/id/OIG.UmTcTiD5tJbm7V26YTp.?w=270&h=270&c=6&r=0&o=5&pid=ImgGn")
    MyEmbed.add_field(name = "!query", value = "Đặt câu hỏi cho chat bot", inline = False)
    MyEmbed.add_field(name = "!pm", value = "Nhắn Tin riêng tư với bot.", inline = False)
    await ctx.send(embed = MyEmbed)

@bot.command()
@commands.check(discordUtil.is_me)
async def unloadGemini(ctx):
    await bot.remove_cog('GeminiAgent')

@bot.command()
@commands.check(discordUtil.is_me)
async def reloadGemini(ctx):
    await bot.add_cog(GeminiAgent(bot))

async def startcogs():
    await bot.add_cog(GeminiAgent(bot))

asyncio.run(startcogs())
bot.run(os.getenv('DISCORD_TOKEN'))
