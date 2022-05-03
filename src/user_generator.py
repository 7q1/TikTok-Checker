# Developed & Programmed By 7Q1
# iG -> @thrudespair

import random
import time
import os

userName = os.getlogin()
numbers = '0123456789'
abc = 'abcdefghijklmnopqrstuvwxyz_'
all = numbers + abc
passList = []
cwd = os.getcwd()
cwd = cwd + "/user.txt"

# <!---------------------------------------- >
# Pervent ValueError:
try:
  print("\n\n[+] Input Number Only!")
  while True:
    try:
      times = int(input('[?] How many passwords >> '))
      break
    except:
      print("[+] Input Number Only!")
  while True:
    try:
      chr = int(input('[?] How many Character >> '))
      break
    except:
      print("[+] Input Number Only!")
  # Passwords Generator:
  print("\n")
  for i in range(times):
    password = "".join(random.sample(all, chr))
    passList.append(password)
  print("\n")

  for i in passList:
    i = i + "\n"
    with open(cwd, 'a') as f:
      f.write(i)
  input(F"[+] Lists Saved in {os.getcwd()}.\n\nPress Enter To exit . . .")
except KeyboardInterrupt:
  print("\nScript Stopped.")
# <!---------------------------------------- >

