#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

data = cgi.FieldStorage()
show_cmd = data.getvalue("show_list_cmd")

if (("show" in show_cmd) or ("list" in show_cmd)) and (("docker" in show_cmd) or ("container" in show_cmd)) and ("status" not in show_cmd) and ("image" not in show_cmd):
    output = subprocess.getoutput("sudo docker ps")
elif (("show" in show_cmd) or ("list" in show_cmd)) and (("stoped" in show_cmd)):
    output = subprocess.getoutput("sudo docker ps -a")
elif (("show" in show_cmd) or ("list" in show_cmd)) and (("image" in show_cmd)):
    output = subprocess.getoutput("sudo docker images")
elif ("show" in show_cmd) and ("status" in show_cmd):
    output = subprocess.getoutput("sudo systemctl status docker")
else:
    output = "Invalid Entry!"

print(output)
