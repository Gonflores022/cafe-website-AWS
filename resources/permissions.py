'''
	You must replace <bucket-name> with your actual bucket name
'''
import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1")
bucket_name = "c103117a2378096l5494794t1w142021518630-s3bucket-twqzjg33iodk"

policy_file = open("/home/ec2-user/environment/resources/website_security_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("DONE")
