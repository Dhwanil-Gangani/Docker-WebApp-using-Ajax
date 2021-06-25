#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

data = cgi.FieldStorage()
start_cmd = data.getvalue("start_cmd")
image_name = data.getvalue("image_name")
if (("start" in start_cmd) or ("run" in start_cmd)) and (("docker" in start_cmd) or ("container" in start_cmd)) and (image_name != ""):
    output = subprocess.getoutput("sudo docker run -dit {}".format(image_name))
elif ("launch" in start_cmd):
    output = subprocess.getoutput("sudo docker start {}".format(start_cmd))
elif (("download" in start_cmd) or ("install" in start_cmd)) and (image_name != ""):
    output = subprocess.getoutput("sudo docker pull {}".format(image_name))
elif (("search" in start_cmd) or ("find" in start_cmd)) and (image_name != "") and ("docker hub" in start_cmd):
    output = subprocess.getoutput("sudo docker search {}".format(image_name))
else:
    output = "Invalid Text!"

print(output)
