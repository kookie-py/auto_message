# based on channel id
def getData():
  data = [
    {
      "TOKEN": "abc",
      "MESSAGE": """
      Selling stuffffff

      """,
      "CHANNEL_IDS": [
        [1081265322784460800, 120],
        [1084213228608946238, 120],
        [916391957570404394, 3600],
      ],
    },
    
    ####
    
    {
      "TOKEN": "abc",
      "MESSAGE": """
      selling stuff too
      """,
      "CHANNEL_IDS": [
        # FORMAT: ["Channel ID", seconds to wait],
        [1078455247686619209, 1800],
      ],
    },
  ]
  return data

getData()