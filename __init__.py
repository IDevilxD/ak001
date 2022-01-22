import os

def work(commamd):
  os.system(command)

def change(path):
  os.system("cd {path}")

def m_home():
  os.system("cd /data/data/com.termux/files/home/akash")

def t_home():
  os.system("cd /data/data/com.termux/files/home")

def set():
  m_home()
  os.system("pip install -r requirements.txt")

def stop():
  break
