import os
import re
import sys
import getpass
from thmapi import THM
from datetime import date

# API
thm = THM()

# Room details
room = thm.room_details(sys.argv[1])
room_questions = thm.room_tasks(sys.argv[1])

# Date
today = date.today()
# Textual month, day and year
date = today.strftime("%b %d, %Y")


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


path = room.get('title')

try:
    os.mkdir(path)
except OSError:
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s " % path)

file = open(f"{path}/README.md", "w")
file.write(f"# TryHackMe {room.get('type')}\n\n"
           f"## {room.get('title')}\n\n"
           f"> _{getpass.getuser()} | {date}_\n\n")

for i in room_questions:
    # print(cleanhtml((str(i.get('questions')))), "\n")
    for ii in i.get('questions'):
        if ii.get('questionNo') == 1:
            file.write(f"----------------------------------------\n\n")
            file.write(f"{ii.get('questionNo')}. {cleanhtml(ii.get('question'))}\n\n")
        else:
            file.write(f"{ii.get('questionNo')}. {cleanhtml(ii.get('question'))}\n\n")
        file.write("```\n")
        file.write("")
        file.write("```\n\n")

file.close()
