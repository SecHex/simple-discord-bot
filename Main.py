import discord
import math
from discord.ext import commands
import aiohttp
import asyncio
import datetime



intents = discord.Intents.default()
intents.members=True


#The Bot hates this words!
badwords = ['nigger', 'allah', 'aladin', 'Bastard', 'Nigger', 'Gay', 'gay', 'Hurensohn', 'hurensohn', 'hs', 'HS',]

#Prefix + Description
bot = commands.Bot(command_prefix='+', description="Here u can see the Commands!")




#simple commands
@bot.command()
async def math(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)  
    
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description="createt by ➥𝕽𝖎𝖈𝖐#0666",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.red())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(
        url=
        "https://sun9-74.userapi.com/impg/fvUnmIb3_RQ1PyDjFsmV2LzzsQR0t41BXLIKgQ/8igIze_yqNk.jpg?size=604x548&quality=96&sign=82bc149b41c9653da9109e7dbf98b611&type=album"
    )

    await ctx.send(embed=embed)
    
    
@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send('Na schnuckel!')
 

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send('Bin erstmal raus süße!')        
        
        
@bot.command()
async def clear(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    await ctx.send(f'{limit} messages have been cleared.')    
    
    
@bot.command()
async def send(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
    
    
@bot.command()
async def invite(ctx):
    await ctx.send('**Here is the invite buddy** "discord.gg/3SZZMGFA2T"')
    

@bot.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
      # This time we'll get the fact request as well!
      request2 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request2.json()

   embed = discord.Embed(title="Here daddy... 💦", color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)       
        
        
        
    
    
@bot.event
async def on_message(message):
   for i in badwords: # Go through the list of bad words;
      if i in message.content:
         await message.delete()
         await message.channel.send(f"{message.author.mention} Eyy, little boy! Dont use this word or u get a kick bitch!")
         bot.dispatch('profanity', message, i)
         return # So that it doesn't try to delete the message again, which will cause an error.
   await bot.process_commands(message)    
  
  
@bot.event
async def on_profanity(message, word):
   channel = bot.get_channel(923188255724306443)
   embed = discord.Embed(title="Profanity Alert!",description=f"{message.author.name} just said ||{word}||", color=discord.Color.blurple()) # Let's make an embed!
   await channel.send(embed=embed)
     
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(
        name="https://discord.gg/Pyex77JfQP", url="https://www.twitch.tv/amouranth"))
    print('Im online homie')
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)
        
        
bot.run('#YourBotTokken!!!!!') 
