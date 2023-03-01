import json
import boto3

region = 'us-east-1'
instances = ['i-07f9ceb5b274160a8']
ec2 = boto3.client('ec2', region_name=region)

# starts remote server
def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    for i in range(len(instances)):
        print('Started instance ' + str(i) )