import boto3

region = 'us-east-1'
instances = ['i-07f9ceb5b274160a8']
ec2 = boto3.client('ec2', region_name=region)


# stops remote server
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    for i in range(len(instances)):
        print('Stopped instance ' + str(i))
