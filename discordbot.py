from discord.ext import commands
import os
import traceback
import makeyupoline
bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def yuuta(ctx):
    await ctx.send('いやそれは違うんじゃあないかと。')
    
 @bot.command()
async def fujii(ctx , msg):
    
    img=makeyupoline.img_add_msg("./yupoline.png", msg ,#FF5555,30)
    img.save("./yupoline_res.png")
    await ctx.send(file=discord.File("./yupoline_res.png"))


bot.run(token)
