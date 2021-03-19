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

x = mydata.getvalue("x")

if x == "launch_instance":
    image_id = mydata.getvalue("image_id")
    instance_type = mydata.getvalue("instance_type")
    count = mydata.getvalue("count")
    subnet_id = mydata.getvalue("subnet_id")
    security_group_id = mydata.getvalue("security_group_id")
    key_name = mydata.getvalue("key_name")
    launchInstance(image_id, instance_type, count, subnet_id, security_group_id, key_name)
    print("EC2 instance is being created...")
elif x == "create_ebs_volume":
    availability_zone = mydata.getvalue("availability_zone")
    volume_type = mydata.getvalue("volume_type")
    size = mydata.getvalue("size")
    key = mydata.getvalue("key")
    value = mydata.getvalue("value")
    createEbsVolume(availability_zone, volume_type, size, key, value)
    print("EBS Volume is being created...")
elif x == "attach_ebs_volume":
    volume_id = mydata.getvalue("volume_id")
    instance_id = mydata.getvalue("instance_id")
    device_name = mydata.getvalue("device_name")
    attachEbsVolume(volume_id, instance_id, device_name)
elif x == "upload_to_bucket":
    local_file_location = mydata.getvalue("local_file_location")
    s3_bucket_location = mydata.getvalue("s3_bucket_location")
    acl = mydata.getvalue("acl")
    uploadFileToBucket(local_file_location, s3_bucket_location, acl)
    print("File is being uploaded...")
elif x == "create_distribution":
    bucket_name = mydata.getvalue("bucket_name")
    default_root_object = mydata.getvalue("default_root_object")
    createDistribution(bucket_name, default_root_object)
else:
    print("AWS RESOURCE CREATION FAILED")
