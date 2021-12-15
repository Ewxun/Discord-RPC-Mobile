import requests
import json

def get_img_id(applicationid,imagekey):
  r = requests.get(f"https://discord.com/api/oauth2/applications/{applicationid}/assets")

  apires = r.json()

  #jsond = json.dumps(apires,indent=3)

  for sect in apires:
    if sect["name"] == imagekey:
      return sect["id"]