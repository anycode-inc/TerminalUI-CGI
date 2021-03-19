import subprocess as sp

def createDistribution(bucketName, defaultRootObject):
    sp.getoutput("aws cloudfront create-distribution --origin-domain-name {0}.s3.amazonaws.com --default-root-object {1}".format(bucketName, defaultRootObject))