import subprocess
from urllib.request import urlopen

# function to monitor ping using the systems ping command
def ping_monitor():

  command = "ping"
  ip_adddress = "google.com"
  data = ""

  output = subprocess.Popen([command, ip_adddress], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

  for lines in output.communicate():
    data = data + lines
  print(data)

  # Extract the value using string manipulation
  avg_ping_value = data.split("Average =")[1].split("ms")[0]
  print(avg_ping_value)

  if int(avg_ping_value) >= 150:
    print("Ping is high" + avg_ping_value)
  else:
    print("ping is normal" + avg_ping_value)

  """
  To extract the time value, we use the split() method on the output string. The first split() operation is output.split("Average ="), which splits the string at the substring "Average =". This will result in a list with two elements: the part before "Average =" and the part after "Average =". We are interested in the part after "Average =", so we access it by using [1].

  The next split() operation is split("ms"). We split the second part of the string obtained in the previous step at the substring "ms". This will give us a list with two elements: the time value and the part after "ms". We are interested in the time value, so we access it by using [0].

  """

# function to check whether the internet is connected or not
def check_connection():

  connection = 0
  
  try:
    urlopen("https://www.google.com/", timeout=1)
    connection = 1
  except:
    connection = 0

  if connection == 1:
    print("Connected")
    ping_monitor()
  else:
    print("not connected")