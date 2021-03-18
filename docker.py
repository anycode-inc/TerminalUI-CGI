#!/usr/bin/python3

import subprocess as sp
import cgi

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

task = mydata.getvalue("x")

def confPython():
    res = sp.getoutput(f"sudo docker run centos /bin/bash -c 'dnf install python3 -y; echo \"print('hello')\" > aa.py; python3 aa.py'")
    return res

def confHttpd(image_name):
    res = sp.getoutput(f"sudo docker run {image_name} /bin/bash -c 'dnf install httpd -y; /usr/sbin/httpd'")
    return res

if task == "python":
    confPython()
    print("PYTHON SUCCESS")
elif task == "httpd":
    image_name = mydata.getvalue("image_name")
    confHttpd(image_name)
    print("HTTPD SUCCESS")
else:
    print("FAILED")
