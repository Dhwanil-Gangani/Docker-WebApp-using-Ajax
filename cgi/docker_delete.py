#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

data = cgi.FieldStorage()
delete_cmd = data.getvalue("delete_cont_cmd")
delete_image_name = data.getvalue("delete_image_name")

if (("delete" in delete_cmd) or ("remove" in delete_cmd)) and ("image" in delete_cmd) and (delete_image_name != "") and ("all" not in delete_cmd) and ("conatiner" not in delete_cmd):
    output = subprocess.getoutput("sudo docker rmi -f {}".format(delete_image_name))
elif (("delete" in delete_cmd) or ("remove" in delete_cmd)) and ("all" in delete_cmd) and ("image" in delete_cmd):
    output = subprocess.getoutput("sudo docker rmi -f $(docker images -q)")
elif (("delete" in delete_cmd) or ("remove" in delete_cmd)) and ("all" in delete_cmd) and ("container" in delete_cmd):
    output = subprocess.getoutput("sudo docker rm -f $(docker ps -a -q)")
else:
    output = "Invalid Text!"

print(output)
