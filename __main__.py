import os
from akash import *

running = True
while running:
  raw_txt = input("Akash env: ")
  s_txt = raw_txt.split(" ")
  if s_txt[0] == "akash":
    try:
      command = s_txt[1]
      if command == "-u":
        update()
      if command == "-h":
        help()
      if command == "-s":
        set()
      if s_txt[0] == "cd":
        try:
          path = s_txt[1]
        except IndexError:
          h_home()
    except IndexError as range:
      print("Error: No akash command mentioned")
