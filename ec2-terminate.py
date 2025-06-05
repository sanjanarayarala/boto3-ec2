import boto3
from dotenv import load_dotenv
import os

load_dotenv()
instance_id= os.getenv("Instance_IDs")

aws_management_console= boto3.session.Session(profile_name='default')
ec2_console= aws_management_console.client('ec2')

#Start exisiting EC2 instance
response= ec2_console.terminate_instances(InstanceIds= [instance_id])