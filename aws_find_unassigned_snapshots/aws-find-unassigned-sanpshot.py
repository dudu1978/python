import boto3

## Authentication parameters ##
aws_access_key_id = 'Enter your key'
aws_secret_access_key = 'Enter your key'
owner_id_value = 'Enter_your_owner_id_value'
region_name = 'eu-west-1'

## Defined Varibles ##
ami_info = []
ami_snapid = []
ebs_snaplist = []
unassigned_ebs_snaplist =[]
ebs_snaplist_count = 0
ami_snapshot_count = 0
unassigned_snapshots_count = 0

## Create filer ##
filter = [{'Name': 'owner-id', 'Values': [owner_id_value]}]

## Define Connection ##
client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

## Request for Data ##
ami_info_resposnse = client.describe_images(Filters=filter)
snapshot_resposnse = client.describe_snapshots(Filters=filter)

## Get SnapshotID per AMI ##

for image in ami_info_resposnse['Images']:
    dic = {}
    dic['amiID'] = image['ImageId']
    for block_device in image['BlockDeviceMappings']:
        if 'Ebs' in block_device:
            if 'SnapshotId' in block_device['Ebs']:
                ami_snapshot_count = ami_snapshot_count + 1
                if 'SnapshotId' in dic:
                    dic['SnapshotId'].append(block_device['Ebs']['SnapshotId'])
                else:
                    dic['SnapshotId'] = [block_device['Ebs']['SnapshotId']]
    ami_info.append(dic)
#print(ami_info)
print ('Number of Snapshots associated with AMIs: ' + str(ami_snapshot_count))


# Get full EBS snapshot List ##

for snapshot in snapshot_resposnse['Snapshots']:
    ebs_snaplist.append(snapshot['SnapshotId'])
    ebs_snaplist_count = ebs_snaplist_count + 1
#print (ebs_snaplist)
print ('Number of Ebs Snapshots: ' + str(ebs_snaplist_count))


### Find SnapshotID that are not assigned to AMI ##

for ami_data in ami_info:
    for snapshotid in ami_data['SnapshotId']:
        ami_snapid.append(snapshotid)

for snapid in ebs_snaplist:
    if snapid not in ami_snapid:
        # print('AMI Snapid: ' + snapid + ' Not Included in Snapliet')
        unassigned_ebs_snaplist.append(snapid)
        unassigned_snapshots_count = unassigned_snapshots_count + 1

print ('Number of unassigned snapshots: ' + str(unassigned_snapshots_count))
print ('List of unassigned snapshots' + str(unassigned_ebs_snaplist))
