import subprocess as sp
from time import sleep

def createEbsVolume(availabilityZone, volumeType, size, key, value):
    command = "aws ec2 create-volume --availability-zone " + availabilityZone + " --volume-type " + volumeType + " --size " + size + " --tag-specifications ResourceType=volume,Tags=[{Key=" + key + ",Value=" + value + "}]"
    sp.getoutput(command)

def attachEbsVolume(volumeID, instanceID, deviceName):
    sp.getoutput("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}".format(volumeID, instanceID, deviceName))