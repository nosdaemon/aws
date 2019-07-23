import boto3
from datetime import date, datetime

# Get all Volumes
def get_volumes():
    ec2 = boto3.resource('ec2')
    all_volume = ec2.volumes.all()
    Response = list()
    for Vol in all_volume:
        Response.append(Vol.attachments[0])
    return Response
