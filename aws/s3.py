import subprocess as sp

def uploadFileToBucket(localFileLocation, s3BucketLocation, acl):
    sp.getoutput("sudo aws s3 cp {0} {1} --acl {2}".format(localFileLocation, s3BucketLocation, acl))