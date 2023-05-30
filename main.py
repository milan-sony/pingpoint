import subprocess
# https://www.datacamp.com/tutorial/python-subprocess
from urllib.request import urlopen
from time import sleep
from notifypy import Notify

# desktop notification
def desktop_notification(title, message):
  notification_title = str(title)
  notification_message = str(message)
  notification = Notify()
  notification.application_name = "PINGPOINT"
  notification.title = notification_title
  notification.message = notification_message
  notification.icon = "./icon2.png"
  # notification.audio = "./.wav"
  notification.send()

# function to monitor ping using the systems ping command
def ping_monitor():

  command = "ping"
  ip_adddress = "google.com"
  ping_value = 100
  data = ""

  output = subprocess.Popen([command, ip_adddress], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

  for lines in output.communicate():
    data = data + lines
  # print(data)

  # Extract the value using string manipulation
  avg_ping_value = data.split("Average =")[1].split("ms")[0]
  # print(avg_ping_value)

  if int(avg_ping_value) > ping_value:
    desktop_notification(
      "❗ High Ping",
      f"Your internet ping is high {avg_ping_value} ms"
    )
    # print("Ping is high" + avg_ping_value)
  else:
    # print("ping is normal" + avg_ping_value)
    pass

  """
  To extract the time value, we use the split() method on the output string. The first split() operation is output.split("Average ="), which splits the string at the substring "Average =". This will result in a list with two elements: the part before "Average =" and the part after "Average =". We are interested in the part after "Average =", so we access it by using [1].

  The next split() operation is split("ms"). We split the second part of the string obtained in the previous step at the substring "ms". This will give us a list with two elements: the time value and the part after "ms". We are interested in the time value, so we access it by using [0].

  """

# function to check whether the internet is connected or not
def check_connection():

  connection = 0

  try:
    urlopen("https://www.google.com/")
    connection = 1
  except:
    connection = 0

  if connection == 1:
    # print("Connected")
    ping_monitor()
  else:
    # print("not connected")
    pass

while True:
  sleep(3)
  check_connection()