import boto3

client = boto3.client('ec2')

#Create VPC
myvpc = client.create_vpc(
	CidrBlock='10.10.0.0/16',
	InstanceTenancy='default',
	TagSpecifications=[{'ResourceType':'vpc','Tags':[{'Key':'Name','Value':'mypyvpc'}]}])
print("Created VPC: ",myvpc['Vpc']['VpcId'])

#Create Subnet
mysubnet = client.create_subnet(
	CidrBlock='10.10.1.0/24',
	AvailabilityZone='us-east-1a',
	VpcId=myvpc['Vpc']['VpcId'],
	TagSpecifications=[{'ResourceType':'subnet','Tags':[{'Key':'Name','Value':'mypysubnet'}]}])
print("Created Subnet: ",mysubnet['Subnet']['SubnetId'])

#Create RouteTable
myrt = client.create_route_table(
	VpcId=myvpc['Vpc']['VpcId'],
	TagSpecifications=[{'ResourceType':'route-table','Tags':[{'Key':'Name','Value':'mypyrt'}]}])
print("Created RouteTable: ",myrt['RouteTable']['RouteTableId'])

#Create InternetGateway
myigw = client.create_internet_gateway(
	TagSpecifications=[{'ResourceType':'internet-gateway','Tags':[{'Key':'Name','Value':'mypyrt'}]}])
print("Created InternetGateway: ",myigw['InternetGateway']['InternetGatewayId'])

#Attach InternetGateway
attachigw = client.attach_internet_gateway(
	VpcId=myvpc['Vpc']['VpcId'],
	InternetGatewayId=myigw['InternetGateway']['InternetGatewayId'])
print("Attached InternetGateway")

#SubnetAssociation
subnetassoc = client.associate_route_table(
	RouteTableId=myrt['RouteTable']['RouteTableId'],
	SubnetId=mysubnet['Subnet']['SubnetId'])
print("Associated Subnet")

#RouteEntry
igwroute = client.create_route(
	DestinationCidrBlock='0.0.0.0/0',
	RouteTableId=myrt['RouteTable']['RouteTableId'],
	GatewayId=myigw['InternetGateway']['InternetGatewayId'])
print("Added IGWroute")