import os
import sys
import boto3
import time

def lambda_handler(client, snap): 
    client = boto3.client('ec2')
    a =  client.describe_instances(Filters = [{'Name': 'tag-value', 'Values': ['Critical']}])
    b = a.get('Reservations')
    for i in b:
        inst = i.get('Instances')
	for j in inst:
		insid = j.get('InstanceId')
		tagname=client.describe_tags(Filters=[{'Name':'key','Values':['Name']},{'Name':'resource-id','Values':[insid]}])
		tag=tagname.get('Tags')
		for t in tag:
			name=t.get('Value')
			instate = j.get('State')
			status = instate.get('Name')
			attr = client.describe_instance_attribute(InstanceId=insid, Attribute='blockDeviceMapping')
			blk = attr.get('BlockDeviceMappings')
			if status == 'running' or status == 'stopped' :
				for l in blk:
					ebs = l.get('Ebs')
					vol = ebs.get('VolumeId')
					snap = client.create_snapshot(VolumeId=vol, Description=name + " " + time.asctime( time.localtime(time.time()) ))
	return