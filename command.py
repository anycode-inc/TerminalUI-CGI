#!/usr/bin/python3

import subprocess as sp
import cgi

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

command = mydata.getvalue("command")

def run_command():
    res = sp.getoutput(f"{command}")
    print(res)

run_command()
