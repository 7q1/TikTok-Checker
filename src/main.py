import os
import atexit
try:
    import requests
except:
    os.system("pip install requests")
try:
    import colorama
except:
    os.system("pip install colorama")
import threading
import requests
import time
from os import sys
from colorama import *
from tkinter import *
from tkinter import messagebox

os.system("cls||clear")

# github.com/7q1 
logo = (F"""{Fore.CYAN}

╔══════╗  ╔════════╗      ╔═╗
╚════╗ ║  ║ ╔════╗ ║     ╔  ║
    ╔╝╔╝  ║ ║ ╔╗ ║ ║   ╔═╝  ║
   ╔╝╔╝   ╚╗  ╔╗  ╔╝   ╚═╝  ║  
  ╔╝╔╝     ╚═╗  ╔═╝         ╚═╗
  ╚═╝        ╚══╝     ╚══════╝{Fore.RESET}""")


# Start

try:
    file = open("user.txt", "r")
except FileNotFoundError:
    sys.exit("File [user.txt] Not Found!\nRun [user_generator.py] To create new user.txt List.\n")

print("TikTok Checker By\n" + logo + "\n")
print(F"[{Fore.MAGENTA}!{Fore.RESET}] Available usernames could be banned.")

threadNum = int(input(F"[{Fore.YELLOW}?{Fore.RESET}] Threads Number [1-10] > "))

while not 0 < threadNum <= 10:
    threadNum = int(input(F"[{Fore.YELLOW}?{Fore.RESET}] Threads Number [1-10] > "))
print()

# Messagebox after script finish
@atexit.register
def messageBox():
    window = Tk()
    window.wm_attributes('-topmost', True)
    window.overrideredirect(1)
    window.withdraw()
    messagebox.showinfo("Finished", "\tChecker Finished ✓\t")
# Checker function
def func():
    while 1:
        user = file.readline().split("\n")[0]
        # Exit loop when there's no user left.
        if user == "":
            break

        with requests.Session() as s:
            r = s.head(F"https://www.tiktok.com/@{user}").status_code

            if r == 200:
                print(F"[{Fore.RED}-{Fore.RESET}] Unavailable --> {user}")
            elif r == 404:
                print(F"[{Fore.GREEN}+{Fore.RESET}] Available --> {user}")
                with open("found.txt", "a") as f:
                    f.write(F"{user}\n")
            else:
                print(F"Error code: {r}")

# Threads
for i in range(threadNum):
    t = threading.Thread(target = func)
    t.start()


# - exit(0)
