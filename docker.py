#!/usr/bin/python3

import subprocess as sp
import cgi

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

task = mydata.getvalue("x")

if task == "python":
    confPython()
    print("SUCCESS")
elif task == "httpd":
    image_name = mydata.getvalue("image_name")
    confHttpd(image_name)
    print("HTTPD SUCCESS")

def confPython():
    sp.run(f"sudo docker run centos /bin/bash -c 'dnf install python3 -y; echo \"print('hello')\" > aa.py; python3 aa.py'",shell=True)

def confHttpd(image_name):
    sp.run(f"sudo docker run {image_name} /bin/bash -c 'dnf install httpd -y; /usr/sbin/httpd'", shell=True)
