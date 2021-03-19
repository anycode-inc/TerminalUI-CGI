#!/usr/bin/python3

import subprocess as sp
import cgi

from ec2_instance import launchInstance
from ebs import createEbsVolume, attachEbsVolume
from s3 import uploadFileToBucket
from cloudfront import createDistribution

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

task = mydata.getvalue("x")

if x == "launch_instance":
    launchInstance(image_id, instance_type, count, subnet_id, security_group_id, key_name)
    print("EC2 instance is being created...")
elif x == "create_ebs_volume":
    createEbsVolume(availabilityZone, volumeType, size, key, value)
    print("EBS Volume is being created...")
elif x == "attach_ebs_volume":
    attachEbsVolume(volumeID, instanceID, deviceName)
elif x == "upload_to_bucket":
    uploadFileToBucket(localFileLocation, s3BucketLocation, acl)
    print("File is being uploaded...")
elif x == "create_distribution":
    createDistribution(bucketName, defaultRootObject)
else:
    print("AWS RESOURCE CREATION FAILED")