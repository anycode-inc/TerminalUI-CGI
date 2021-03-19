#!/usr/bin/python3

import subprocess as sp
from jinja2 import Environment, FileSystemLoader
import time
import cgi

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

node = mydata.getvalue("node")

def configure_kube_master_playbook(pod_network_cidr, owner, group):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader = file_loader)
    template = env.get_template('kube_master.yml.j2')
    output = template.render(pod_network_cidr = pod_network_cidr , owner = owner, group = group)
    file = open("./temp/kube_master.yml", "w")
    file.write("%s" %(output))
    file.close()

def configure_kube_slave_playbook(kube_join_command):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader = file_loader)
    template = env.get_template('kube_slave.yml.j2')
    output = template.render(kube_join_command = kube_join_command)
    file = open("./temp/kube_slave.yml", "w")
    file.write("%s" %(output))
    file.close()

if node == "master":
    pod_network_cidr = mydata.getvalue("pod_network_cidr")
    owner = mydata.getvalue("owner")
    group = mydata.getvalue("group")
    configure_kube_master_playbook(pod_network_cidr, owner, group)
    sp.run("ansible-playbook ./temp/kube_master.yml", shell=True)
    print("KUBE MASTER CONFIGURATION SUCCESSFUL")
elif node == "slave":
    kube_join_command = mydata.getvalue("kube_join_command")
    configure_kube_slave_playbook(kube_join_command)
    sp.run("ansible-playbook ./temp/kube_slave.yml", shell=True)
    print("KUBE SLAVE CONFIGURATION SUCCESSFUL")
else:
    print("KUBE CLUSTER CONFIGURATION FAILED")