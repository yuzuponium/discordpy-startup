from discord.ext import commands
import os
import traceback
import makeyupoline
import discord
from PIL import Image, ImageFont, ImageDraw
bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.command()
async def yuuta(ctx):
    await ctx.send('いやそれは違うんじゃあないかと。')
    
@bot.command()
async def hima(ctx,msg='a'):
    answer='漫画読もう'
    if 'ゲーム' in msg:
        answer='VALORANT'
    elif msg=='付き合って':
        answer='喜んで♡'
    elif msg='うんこ':
        answer='カレーのことかな？'
    await ctx.send(answer)
    
@bot.command()
async def fujii(ctx , msg):
    
    img=makeyupoline.img_add_msg("./yupoline.png", msg ,"#FF5555",30)
    img.save("./yupoline_res.png")
    await ctx.send(file=discord.File("./yupoline_res.png"))


bot.run(token)
