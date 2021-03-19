import subprocess as sp

def launchInstance(image_id, instance_type, count, subnet_id, security_group_id, key_name):
<<<<<<< HEAD
    sp.getoutput("aws ec2 run-instances --image-id {0} --instance-type {1} --count {2} --subnet-id {3} --security-group-ids {4} --key-name {5} --user-data file://aws/ud.txt".format(image_id, instance_type, count, subnet_id, security_group_id, key_name))
=======
    sp.getoutput("aws ec2 run-instances --image-id {0} --instance-type {1} --count {2} --subnet-id {3} --security-group-ids {4} --key-name {5}".format(image_id, instance_type, count, subnet_id, security_group_id, key_name))
>>>>>>> 8921f562826de180c4f9fe87c0d4855ddf8d4f7c
