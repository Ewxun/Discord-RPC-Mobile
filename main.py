import os
import time
import asyncio

import discord
from discord.ext import commands
import yaml

with open("config.yml","r") as file:
  config = yaml.full_load(file.read())


from ext.imgid import get_img_id
from ext.mcstat import mcstats
if config["replit"]:
  from ext.bot_stat import keep_on
  keep_on()
  token = os.environ.get("TOKEN")
else:
  token = config["token"]


# Initialization
appid = config["application_id"]
imgdic = None
starttime = None
partyd = None
timed = None


bot = commands.Bot(command_prefix='xxxx', intents=discord.Intents.all(), case_insensitive=True)


try:
  if config["images"]["enable_images"] in [True,"true","True"]:  
    imgdic = dict([
      ("large_image", get_img_id(appid,config["images"]["large_image_key"])), 
      ("large_text", config["images"]["large_image_text"]),
      ("small_image", get_img_id(appid,config["images"]["small_image_key"])),
      ("small_text", config["images"]["small_image_text"])
     ]) 

except TypeError:
  print("\n")
  raise TypeError("Application ID needed to use art assets / images.")


if config["party"]["enable_party"] in [True,"true","True"]:
  if config["party"]["minecraft"]["enable_detection"]:
    if config["party"]["minecraft"]["server_port"] != None:
      servermergip = config["party"]["minecraft"]["server_ip"] + ":" + str(config["party"]["minecraft"]["server_port"])
    else:
      servermergip = config["party"]["minecraft"]["server_ip"] + ":25565"
    partylist = mcstats(servermergip)
    #print(partylist)
    partyd = dict([
      ("id",None),
      ("size",partylist)
    ])
  
  elif config["party"]["minecraft"]["enable_detection"] in [False,"False","false"]:
    partyd = dict([
      ("id",None),
      ("size",[int(config["party"]["party_current_size"]), int(config["party"]["party_max_size"])])])


if config["elapsed_time"]["enable_elapsed_time"] in [True,"True","true"]:
  if config["elapsed_time"]["mode"].lower() == "normal":
    starttime = int(time.time())*1000
    timed = dict([("start",starttime),("end",None)])
  elif config["elapsed_time"]["mode"].lower() == "custom_start":
    starttime = int(config["elapsed_time"]["start_time"])*1000
    timed = dict([("start",starttime),("end",None)])
  elif config["elapsed_time"]["mode"] == "countdown":
    endtime = int(config["elapsed_time"]["end_time"])*1000
    timed = dict([("start",None),("end",endtime)])


async def update_mc():
  if config["party"]["enable_party"] == True and config["party"]["minecraft"]["enable_detection"] == True:
    while True:
      if config["party"]["enable_party"] in [True,"true","True"]:
        if config["party"]["minecraft"]["enable_detection"] == True:
          servermergip = config["party"]["minecraft"]["server_ip"] + ":" + str(config["party"]["minecraft"]["server_port"])
          partylist = mcstats(servermergip)
          #print(partylist)
          partyd = dict([
          ("id",None),
          ("size",partylist)
        ])
  
      act = discord.Activity(
          application_id=appid,
          name=config["game"],
          type = discord.ActivityType.playing,
          state= config["state"],
          details=config["details"],
          assets=imgdic,
          party=partyd,
          timestamps=timed
        )
  
      await bot.change_presence (activity=act)
      await asyncio.sleep(15)
  

@bot.event
async def on_ready():
    print("—————————————————————————")
    print("RPC Set")
    
    act = discord.Activity(
      application_id=appid,
      name=config["game"],
      type = discord.ActivityType.playing,
      state=config["state"],
      details=config["details"],
      assets=imgdic,
      party=partyd,
      timestamps=timed
    )
  
    await bot.change_presence(activity=act)
    bot.loop.create_task(update_mc())

  
@bot.event
async def on_disconnect():
  print("Rich Presence Stopped")

bot.run(token,bot = False)