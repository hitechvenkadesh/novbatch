#PythonBoto3_EC2
import boto3

client = boto3.client('ec2')

def startec2():
	start = client.start_instances(
	InstanceIds=['i-076ad0124e02623a4'])

startec2()


#Lambda_EC2_Stop
import boto3

client = boto3.client('ec2',region_name='us-east-1')

def lambda_handler(event, context):
	stop = client.stop_instances(
	InstanceIds=['i-03998636e2c318dfb','i-076ad0124e02623a4'])