
from discord.ext import commands
import os
import traceback
import random
import asyncio #sleepを使うのに必要

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, message, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())



@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def homeharu(ctx):
    await ctx.send('卍sexyryo卍')

@bot.event
async def on_message(message):
  if message.content == "スロット":
  kakuritsu = random.randint(1, 399)
  slot_list = [':yamasho:', ':NK_3rd:', ':NK_2nd:', ':mocchiup:', ':higasho:', ':domenfuuuuck:', ':ganjaR:']
  A = random.choice(slot_list)
  B = random.choice(slot_list)
  C = random.choice(slot_list)
  if int(kakuritsu) == int(1): #確率は1/399
  await client.send_message(message.channel, "イク！")
  await asyncio.sleep(2) #2秒間待ってやる
  await client.send_message(message.channel, ':abe:', ':abe:', ':abe:') #abeだけ出るように指定
  else:
  await client.send_message(message.channel, "%s%s%s" % (A, B, C))    
    
    
    
    
bot.run(token)
