import os
from akash import *

running = True
while running:
  raw_txt = input("Akash env: ")
  s_txt = raw_txt.split(" ")
  if s_txt[0] == "akash":
    command = s_txt[1]
    if command == "-u" or "--update":
      update()
    if command == "-h" or "--help":
      help()
