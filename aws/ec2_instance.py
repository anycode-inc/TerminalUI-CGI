import subprocess as sp

def launchInstance(image_id, instance_type, count, subnet_id, security_group_id, key_name):
    sp.run("aws ec2 run-instances --image-id {0} --instance-type {1} --count {2} --subnet-id {3} --security-group-ids {4} --key-name {5} --user-data file://aws/ud.txt".format(image_id, instance_type, count, subnet_id, security_group_id, key_name), shell=True)