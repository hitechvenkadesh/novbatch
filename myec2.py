import boto3
import sys

region = sys.argv[1]
access_key = sys.argv[2]
secret_key = sys.argv[3]

ec2 = boto3.client('ec2',
        region_name = region,
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key)

list = ec2.describe_instances()

for output in list['Reservations']:
    for printinsid in output['Instances']:
        for printtag in printinsid['Tags']:
            print(printinsid['InstanceId'],
                printinsid['InstanceType'],
                printinsid['LaunchTime'],
                printinsid['State']['Name'],
                printtag['Value'])
