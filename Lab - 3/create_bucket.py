import boto3

s3 = boto3.client('s3')
bucket_name = 'is698-lab3c'
response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
print(f'Bucket {bucket_name} created successfully!')


