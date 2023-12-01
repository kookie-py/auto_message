# based on channel name
from edit import getData
import requests, time, threading

getdata = getData()
for data in getdata: # loop through each account
  def funcbefore():
    sessionDiscord = requests.Session()
    sessionDiscord.headers["authorization"] = data['TOKEN'] # login to discord
    
    def findchannelbyname(GUILD_ID, channel_name):
      res = sessionDiscord.get(f'https://discord.com/api/v9/guilds/{GUILD_ID}/channels') # send message
      channel_id = None
      for i in res.json():
        if i['name'] == channel_name:
          channel_id = i['id']
          break
      return channel_id
    
    message = data['MESSAGE']
    channels = data['CHANNEL_INFO']
    for i in channels: # get channel ids & time to wait
      def func():
        serverID = i[0] # get server id
        channel_name = i[1] # get channel name
        waits = i[2] # get time to wait
        cid = findchannelbyname(GUILD_ID=serverID, channel_name=channel_name)
        while True: # run script continuously
          sendMSG = sessionDiscord.post(f'https://discord.com/api/v9/channels/{cid}/messages', json={'content': message}) # send message
          if sendMSG.status_code == 404:
            cid = findchannelbyname(GUILD_ID=serverID, channel_name=channel_name)
          time.sleep(waits) # wait x seconds
      threading.Thread(target=func).start() # run function in a new loop
    res = sessionDiscord.get("https://discord.com/api/v9/users/@me")
    user = res.json()['username']
    disc = res.json()['discriminator']
    print(f"[{user}#{disc}] is now running.")
  threading.Thread(target=funcbefore).start()