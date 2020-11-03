import boto3

ec2 = boto3.client('ec2',
        region_name = "us-east-1",
        aws_access_key_id = "AKIAJQABXSEEPAEJ4LHA",
        aws_secret_access_key = "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")

list = ec2.describe_instances()

for output in list['Reservations']:
    for printinsid in output['Instances']:
        for printtag in printinsid['Tags']:
            print(printinsid['InstanceId'],
                printinsid['InstanceType'],
                printinsid['LaunchTime'],
                printinsid['State']['Name'],
                printtag['Value'])