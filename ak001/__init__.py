import os
import random
import requests as r
import datetime as dt
from .vars import *

repo = "https://github.com/IDevilxD/akash"
rm_cmd = "rm -rf akash"

def work(commamd):
  os.system(command)

def change(path):
  os.system(f"cd {path}")

def m_home():
  os.system("cd /data/data/com.termux/files/home/akash")

def t_home():
  os.system("cd /data/data/com.termux/files/home")

def set():
  m_home()
  os.system("pip install -r requirements.txt")

def update():
  os.system(f"{rm_cmd} && git clone {repo} && cd")

def help():
  print(help_txt)

def clear():
  os.system("clear")

def pwd():
  os.system("pwd")

def gett(link,fname):
  raw = r.get(link).text
  file = open("/data/data/com.termux/files/home/akash/websites/{fname}.txt","w")
  file.write(raw)
