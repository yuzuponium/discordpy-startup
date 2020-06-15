from discord.ext import commands
import os
import traceback

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
async def urlimg(ctx, *args):
    message = args[1] 
    message = message.replace('_',' ')
    if len(args) == 2:
        fontcolor = '#FF5555'
    else:
        fontcolor = args[2]
    imgurl = args[0]
    file_name = C:\Users\藤井　佑太\Pictures\Saved Pictures
    r = requests.get(imgurl)
    img = Image.open(io.BytesIO(r.content))
    img.save(file_name)
    img ='.1591974976382 .img_add_msg(file_name, message,fontcolor)
    img.save("./images/result.png")
    await ctx.send(file=discord.File("./images/result.png"))


bot.run(token)
