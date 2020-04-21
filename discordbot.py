
from discord.ext import commands
import os
import traceback
import random
import asyncio #sleepを使うのに必要

bot = commands.Bot()
token = os.environ['DISCORD_BOT_TOKEN']


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
  if message.content == "スロット":
  slot_list = [':yamasho:', ':NK_3rd:', ':NK_2nd:', ':mocchiup:', ':higasho:', ':domenfuuuuck:', ':ganjaR:']
  A = random.choice(slot_list)
  B = random.choice(slot_list)
  C = random.choice(slot_list)
    await bot.send_message(message.channel, "%s%s%s" % (A, B, C))    

    #kakuritsu = random.randint(1, 399)
    #  if int(kakuritsu) == int(1): #確率は1/399
    #      await bot.send_message(message.channel, "イク！")
    #      await asyncio.sleep(2) #2秒間待ってやる
    #      await bot.send_message(message.channel, ':abe:', ':abe:', ':abe:') #abeだけ出るように指定
    #          else:
   
bot.run(token)
