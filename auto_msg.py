# your discord token
TOKEN = "..."

# your trading message
MESSAGE = """
Trading:
Frost drag for x robux
shadow drag for x $$$
"""

# channel ids and cooldown in seconds
CHANNEL_IDS = [
  # Example: {Channel ID, Cooldown in Secs} -> {970622183657320558, 30}
  [1046431872592388156, 5],
  [1046431909070245979, 15],
  [1046431923817435156, 25],
]

#############################
# DONT TOUCH ANYTHING BELOW #
#############################

import requests, time, threading
sessionDiscord = requests.Session()
sessionDiscord.headers["authorization"] = TOKEN # login to discord
threads = []
for i in CHANNEL_IDS: # get channel ids & time to wait
  def func():
    cid = i[0] # get channel id
    waits = i[1] # get time to wait
    while True: # run script continuously
      sessionDiscord.post(f'https://discord.com/api/v9/channels/{cid}/messages', json={'content': MESSAGE}) # send message
      time.sleep(waits) # wait x seconds
  threading.Thread(target=func).start() # run function in a new loop
print("Program is running")
