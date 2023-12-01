# based on channel id
from edit import getData
import requests, time, threading

getdata = getData()
for data in getdata:
  def funcbefore():
    sessionDiscord = requests.Session()
    sessionDiscord.headers["authorization"] = data['TOKEN'] # login to discord
    message = data['MESSAGE']
    channels = data['CHANNEL_IDS']
    for i in channels: # get channel ids & time to wait
      def func():
        cid = i[0] # get channel id
        waits = i[1] # get time to wait
        while True: # run script continuously
          print(message)
          sessionDiscord.post(f'https://discord.com/api/v9/channels/{cid}/messages', json={'content': message}) # send message
          time.sleep(waits) # wait x seconds
      threading.Thread(target=func).start() # run function in a new loop
    res = sessionDiscord.get("https://discord.com/api/v9/users/@me")
    user = res.json()['username']
    disc = res.json()['discriminator']
    print(f"[{user}#{disc}] is now running.")
  threading.Thread(target=funcbefore).start()