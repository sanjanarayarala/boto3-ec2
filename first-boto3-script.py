#Script to get all IAM users
import boto3
from pprint import pprint
aws_management_console= boto3.session.Session(profile_name='default')
iam_console_resource= aws_management_console.resource('iam')
iam_console_client= aws_management_console.client('iam')

# Resource object
for each_user in iam_console_resource.users.all():
    print(each_user.name)

# Client object
for each in iam_console_client.list_users()['Users']:
    print(each['UserName'])

#another way
result = iam_console_client.list_users()
#pprint(result)
pprint(result['Users'])
for users in result['Users']:
    print(users['UserName'])

    