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
      if command == "-g":
        link = input("Enter target name: ")
        fname = input("Enter a name: ")
        gett()
        print("You Can get this websites code in /data/data/com.termux/files/home/akash/websites/{fname}.txt")
      if command == "-h":
        help()
      if command == "-s":
        set()
      if s_txt[0] == "cd":
        try:
          path = s_txt[1]
          print(path)
          cd(path)
        except IndexError:
          m_home()
      if s_txt[0] == "pwd":
        pwd()
    except IndexError as range:
      print("Error: No akash command mentioned")
