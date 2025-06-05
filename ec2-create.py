import boto3
from dotenv import load_dotenv
import os

load_dotenv()
ami_id= os.getenv("AMI_ID")

aws_management_console= boto3.session.Session(profile_name='default')
ec2_console= aws_management_console.client('ec2')

#Creating EC2 instance
response= ec2_console.run_instances(ImageId= ami_id,
                                    InstanceType='t2.micro',
                                    MaxCount=1,
                                    MinCount=1)

