import os
import re
import sys
import getpass
from thmapi import THM
from datetime import date

# API
thm = THM()

full_readme = False

# Room details
for arg in sys.argv:
    if arg == "-r":
        room = thm.room_details(sys.argv[(sys.argv.index(arg) + 1)])
        room_questions = thm.room_tasks(sys.argv[(sys.argv.index(arg) + 1)])
    if arg == "-A":
        full_readme = True

# Date
today = date.today()
# Textual month, day and year
date = today.strftime("%b %d, %Y")


def clean_html(raw_html):
    clean_r = re.compile('<.*?>')
    clean_text = re.sub(clean_r, '', raw_html)
    return clean_text


path = room.get('title')

try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)

if full_readme:
    file = open(f"{path}\README.md", "w")
    file.write(f"# TryHackMe {room.get('type')}\n\n"
               f"## {room.get('title')}\n\n"
               f"> _{getpass.getuser()} | {date}_\n\n")
    file.write(f"---\n\n")
    file.write(f"###Info:\n\n")
    file.write(f"Scans (Nmap, Rust, etc...):\n\n")
    file.write("```\n")
    file.write("")
    file.write("```\n\n")
    file.write(f"System Info (Nikto, WPScan etc...):\n\n")
    file.write("```\n")
    file.write("")
    file.write("```\n\n")
    file.write(f"Directory Scan (Dirb, Dirbuster, etc...):\n\n")
    file.write("```\n")
    file.write("")
    file.write("```\n\n")
    file.write(f"Users And Passwords (Hydra, BurpSuite, etc...):\n\n")
    file.write("```\n")
    file.write("")
    file.write("```\n\n")
    file.write(f"###Questions:\n\n")

    for i in room_questions:
        for ii in i.get('questions'):
            if ii.get('questionNo') == 1:
                file.write(f"----------------------------------------\n\n")
                file.write(f"{ii.get('questionNo')}. {clean_html(ii.get('question'))}\n\n")
            else:
                file.write(f"{ii.get('questionNo')}. {clean_html(ii.get('question'))}\n\n")
            file.write("```\n")
            file.write("")
            file.write("```\n\n")

    file.close()

else:
    file = open(f"{path}\README.md", "w")
    file.write(f"# TryHackMe {room.get('type')}\n\n"
               f"## {room.get('title')}\n\n"
               f"> _{getpass.getuser()} | {date}_\n\n")

    for i in room_questions:
        for ii in i.get('questions'):
            if ii.get('questionNo') == 1:
                file.write(f"----------------------------------------\n\n")
                file.write(f"{ii.get('questionNo')}. {clean_html(ii.get('question'))}\n\n")
            else:
                file.write(f"{ii.get('questionNo')}. {clean_html(ii.get('question'))}\n\n")
            file.write("```\n")
            file.write("")
            file.write("```\n\n")

    file.close()
