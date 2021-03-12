#!/usr/bin/python3

import subprocess as sp
import cgi

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

if mydata.getvalue("x") == "python":
    confPython()
    print("SUCCESS")

def confPython():
    sp.run(f"sudo docker run centos /bin/bash -c 'dnf install python3 -y; echo \"print('hello')\" > aa.py; python3 aa.py'",shell=True)
