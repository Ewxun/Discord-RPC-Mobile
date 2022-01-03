import requests

def mcstats(servip):
  serverip = servip.replace(":25565","")
  
  onpy = requests.get(f"https://mcapi.xdefcon.com/server/{serverip}/players/json").json()

  maxpy = requests.get(f"https://mcapi.xdefcon.com/server/{serverip}/maxplayers/json").json()

  onplayer = int(onpy["players"])
  maxplayer = int(maxpy["maxplayers"])

  return [onplayer,maxplayer]