import boto3

# Initialize S3 client
s3 = boto3.client('s3', region_name='eu-central-1')

# List objects in the S3 bucket
bucket_name = 'road-shutter-bucket'
objects = s3.list_objects_v2(Bucket=bucket_name, Prefix='raw/')

# Iterate over the objects and access the metadata of the images
for obj in objects['Contents']:
    key = obj['Key']
    # Read the image metadata
    response = s3.head_object(Bucket=bucket_name)
    metadata = response['Metadata']

    # Print the metadata
    print('Metadata for image:', key)
    for key, value in metadata.items():
        print(key, ':', value)
    print()