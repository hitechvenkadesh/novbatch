import boto3

region = str(input("Type the Region Code: "))
access_key = str(input("Type your_aws_access_key_id: "))
secret_key = str(input("Type your_aws_secret_access_key: "))

ec2 = boto3.client('ec2',
	region_name = region,
	aws_access_key_id = access_key,
	aws_secret_access_key = secret_key)

list = ec2.describe_instances()
for output in list['Reservations'
	for printinsid in output['Instances']:
		print(printinsid['InstanceId'],
		printinsid['InstanceType'],
		printinsid['LaunchTime'],
		printinsid['State']['Name'])