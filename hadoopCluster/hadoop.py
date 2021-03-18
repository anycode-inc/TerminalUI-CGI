#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import subprocess
import cgi

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

namenode_ip = mydata.getvalue("namenode_ip")
namenode_port = mydata.getvalue("namenode_port")
namenode_directory = mydata.getvalue("namenode_directory")
datanode_ip = mydata.getvalue("datanode_ip")
datanode_directory = mydata.getvalue("datanode_directory")

def installtionScript(nodeType,directoryPath):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('installationScript.sh.j2')
    output = template.render(nodeType = nodeType , directoryPath = directoryPath)
    file = open("./temp/installationScript.sh", "w")
    file.write("%s" %(output))
    file.close()

def hdfsSite(nodeType,directoryPath):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('hdfs-site.xml.j2')
    output = template.render(nodeType = nodeType , directoryPath = directoryPath)
    file = open("./temp/hdfs-site.xml", "w")
    file.write("%s" %(output))
    file.close()

def coreSite(nodeIp,nodePort):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('core-site.xml.j2')
    output = template.render(IP = nodeIp , port = nodePort)
    file = open("./temp/core-site.xml", "w")
    file.write("%s" %(output))
    file.close()

def copyTemplate(nodeIP):
    subprocess.run(f'scp ./temp/hdfs-site.xml root@{nodeIP}:/root/hdfs-site.xml',shell=True)
    subprocess.run(f'scp ./temp/core-site.xml root@{nodeIP}:/root/core-site.xml',shell=True)

def nameNode(nameNodeIP):
    nameNodeDirectory = namenode_directory
    nameNodePort = namenode_port
    hdfsSite('name',f'/root/{nameNodeDirectory}')
    coreSite(nameNodeIP,nameNodePort)
    copyTemplate(nameNodeIP)
    installtionScript('name',nameNodeDirectory)
    subprocess.run(f"ssh root@{nameNodeIP} 'bash -s' < ./temp/installationScript.sh",shell=True)
    return nameNodePort

def dataNode(dataNodeIP,nameNodeIP,nameNodePort):
    dataNodeDirectory = datanode_directory
    hdfsSite('data',f'/root/{dataNodeDirectory}')
    coreSite(nameNodeIP,nameNodePort)
    copyTemplate(dataNodeIP)
    installtionScript('data',dataNodeDirectory)
    subprocess.run(f"ssh root@{dataNodeIP} 'bash -s' < ./temp/installationScript.sh",shell=True)

def configure():
    nameNodeIP = namenode_ip
    dataNodeIP = datanode_ip
    nameNodePort = nameNode(nameNodeIP)
    dataNode(dataNodeIP,nameNodeIP,nameNodePort)
    print("HADOOP CLUSTER SUCCESS")

configure()